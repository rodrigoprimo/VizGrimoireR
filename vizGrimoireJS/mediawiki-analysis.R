## Copyright (C) 2012, 2013 Bitergia
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
##
## This file is a part of the vizGrimoire.R package
##
## Authors:
##   Alvaro del Castillo <acs@bitergia.com>
##
##
## Usage:
##  R --vanilla --args -d dbname < mediawiki-analysis.R

library("vizgrimoire")
library("ISOweek")
options(stringsAsFactors = FALSE) # avoid merge factors for toJSON 


conf <- ConfFromOptParse()
SetDBChannel (database = conf$database, user = conf$dbuser, password = conf$dbpassword)

if (conf$granularity == 'years') { 
    period = 'year'
    nperiod = 365
} else if (conf$granularity == 'months') { 
    period = 'month'
    nperiod = 31
} else if (conf$granularity == 'weeks') { 
    period = 'week'
    nperiod = 7
} else if (conf$granularity == 'days'){ 
    period = 'day'
    nperiod = 1
} else {stop(paste("Incorrect period:",conf$granularity))}

# destination directory
destdir <- conf$destination

# multireport
reports=strsplit(conf$reports,",",fixed=TRUE)[[1]]

# BOTS filtered
bots = c('wikibugs','gerrit-wm','wikibugs_','wm-bot','')

#############
# STATIC DATA
#############

# Tendencies
diffsent.365 = GetMediaWikiDiffReviewsDays(period, conf$enddate, 365)
diffsenders.365 = GetMediaWikiDiffAuthorsDays(period, conf$enddate, conf$identities_db, 365)
diffsent.30 = GetMediaWikiDiffReviewsDays(period, conf$enddate, 30)
diffsenders.30 = GetMediaWikiDiffAuthorsDays(period, conf$enddate, conf$identities_db, 30)
diffsent.7 = GetMediaWikiDiffReviewsDays(period, conf$enddate, 7)
diffsenders.7 = GetMediaWikiDiffAuthorsDays(period, conf$enddate, conf$identities_db, 7)


static.data = GetStaticDataMediaWiki(period, conf$startdate, conf$enddate, conf$identities_db)
static.data = merge(static.data, diffsent.365)
static.data = merge(static.data, diffsent.30)
static.data = merge(static.data, diffsent.7)
static.data = merge(static.data, diffsenders.365)
static.data = merge(static.data, diffsenders.30)
static.data = merge(static.data, diffsenders.7)


createJSON (static.data, paste(destdir,"/mediawiki-static.json", sep=''))

###################
# EVOLUTIONARY DATA
###################

evol_data = GetEvolDataMediaWiki(period, conf$startdate, conf$enddate, conf$identities_db)
evol_data <- completePeriodIds(evol_data, conf$granularity, conf)
createJSON (evol_data, paste(destdir,"/mediawiki-evolutionary.json", sep=''))

#######
# TOPS
#######

top_authors <- list()
top_authors[['authors.']] <- GetTopAuthorsMediaWiki(0, conf$startdate, conf$enddate, conf$identities_db, bots, conf$npeople)
top_authors[['authors.last year']]<- GetTopAuthorsMediaWiki(365, conf$startdate, conf$enddate, conf$identities_db, bots, conf$npeople)
top_authors[['authors.last month']]<- GetTopAuthorsMediaWiki(31, conf$startdate, conf$enddate, conf$identities_db, bots, conf$npeople)
createJSON (top_authors, paste(destdir,"/mediawiki-top.json", sep=''))


###################
# PEOPLE
###################
if ('people' %in% reports){
    all.top.authors <- top_authors[['authors.']]$id
    all.top.authors <- append(all.top.authors, top_authors[['authors.last year']]$id)
    all.top.authors <- append(all.top.authors, top_authors[['authors.last month']]$id)             
    all.top.authors <- unique(all.top.authors)
    createJSON(all.top.authors, paste(destdir,"/mediawiki-people.json",sep=''))

    for (upeople_id in all.top.authors){
        evol = GetEvolPeopleMediaWiki(upeople_id, period, conf$startdate, conf$enddate)
        evol <- completePeriodIds(evol, conf$granularity, conf)
        evol[is.na(evol)] <- 0
        createJSON(evol, paste(destdir,"/people-",upeople_id,"-mediawiki-evolutionary.json", sep=''))

        static <- GetStaticPeopleMediaWiki(upeople_id, conf$startdate, conf$enddate)
        createJSON(static, paste(destdir,"/people-",upeople_id,"-mediawiki-static.json", sep=''))
    }
}




