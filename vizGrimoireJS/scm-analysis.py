#!/usr/bin/env python

# Copyright (C) 2014 Bitergia
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# This file is a part of the vizGrimoire.R package
#
## Authors:
##   Jesus M. Gonzalez-Barahona <jgb@bitergia.com>
##   Alvaro del Castillo San Felix <acs@bitergia.com>
##   Daniel Izquierdo Cortazar <dizquierdo@bitergia.com>
#
# Usage:
#     PYTHONPATH=../vizgrimoire LANG= R_LIBS=../../r-lib ./mls-analysis.py 
#                                                -d acs_irc_automatortest_2388_2 -u root 
#                                                -i acs_cvsanaly_automatortest_2388 
#                                                -s 2010-01-01 -e 2014-01-20 
#                                                -o ../../../json -r people,repositories
#

import logging
from rpy2.robjects.packages import importr
import sys

isoweek = importr("ISOweek")
vizr = importr("vizgrimoire")

import GrimoireUtils, GrimoireSQL
from GrimoireUtils import dataFrame2Dict, createJSON, completePeriodIds
from GrimoireUtils import valRtoPython, read_options, getPeriod
# import MLS

def aggData(period, startdate, enddate, idb, destdir):
#    static_data = GetSCMStaticData(period, conf$startdate, conf$enddate, conf$identities_db)
#    static_url <- StaticURL()
#    diffcommits <- GetDiffCommitsDays(period, conf$enddate, 365)
#    latest_activity7 = last_activity(7)
#    latest_activity14 = last_activity(14)
#    latest_activity30 = last_activity(30)
#    latest_activity60 = last_activity(60)
#    latest_activity90 = last_activity(90)
#    latest_activity180 = last_activity(180)
#    latest_activity365 = last_activity(365)
#    latest_activity730 = last_activity(730)
#
#    diffcommits_365 = GetDiffCommitsDays(period, conf$enddate, 365)
#    diffauthors_365 = GetDiffAuthorsDays(period, conf$enddate, conf$identities_db, 365)
#    diff_files_365 = GetDiffFilesDays(period, conf$enddate, conf$identities_db, 365)
#    diff_lines_365 = GetDiffLinesDays(period, conf$enddate, conf$identities_db, 365)
#
#    diffcommits_30 = GetDiffCommitsDays(period, conf$enddate, 30)
#    diffauthors_30 = GetDiffAuthorsDays(period, conf$enddate, conf$identities_db, 30)
#    diff_files_30 = GetDiffFilesDays(period, conf$enddate, conf$identities_db, 30)
#    diff_lines_30 = GetDiffLinesDays(period, conf$enddate, conf$identities_db, 30)
#
#    diffcommits_7 = GetDiffCommitsDays(period, conf$enddate, 7)
#    diffauthors_7 = GetDiffAuthorsDays(period, conf$enddate, conf$identities_db, 7)
#    diff_files_7 = GetDiffFilesDays(period, conf$enddate, conf$identities_db, 7)
#    diff_lines_7 = GetDiffLinesDays(period, conf$enddate, conf$identities_db, 7)
#
#    community_structure = GetCodeCommunityStructure(period, conf$startdate, conf$enddate, conf$identities_db)
#
#    #Data for specific analysis
#    if ('companies' %in% reports){
#        static_data_companies = evol_info_data_companies (conf$startdate, conf$enddate)
#            static_data = merge(static_data, static_data_companies)
#    }
#    if ('countries' %in% reports){ 
#        static_data_countries = evol_info_data_countries (conf$startdate, conf$enddate)
#            static_data = merge(static_data, static_data_countries)
#    }
#    if ('domains' %in% reports){
#        static_data_domains = evol_info_data_domains (conf$startdate, conf$enddate)
#        static_data = merge(static_data, static_data_domains)
#    }
#    # 2- Merging information
#    static_data = merge(static_data, static_url)
#    static_data = merge(static_data, diffcommits)
#    static_data = merge(static_data, latest_activity7)
#    static_data = merge(static_data, latest_activity14)
#    static_data = merge(static_data, latest_activity30)
#    static_data = merge(static_data, latest_activity60)
#    static_data = merge(static_data, latest_activity90)
#    static_data = merge(static_data, latest_activity180)
#    static_data = merge(static_data, latest_activity365)
#    static_data = merge(static_data, latest_activity730)
#    static_data = merge(static_data, community_structure)
#    static_data = merge(static_data, diffcommits_365)
#    static_data = merge(static_data, diffcommits_30)
#    static_data = merge(static_data, diffcommits_7)
#    static_data = merge(static_data, diffauthors_365)
#    static_data = merge(static_data, diffauthors_30)
#    static_data = merge(static_data, diffauthors_7)
#    static_data = merge(static_data, diff_files_365)
#    static_data = merge(static_data, diff_files_30)
#    static_data = merge(static_data, diff_files_7)
#    static_data = merge(static_data, diff_lines_365)
#    static_data = merge(static_data, diff_lines_30)
#    static_data = merge(static_data, diff_lines_7)
#
#    # 3- Creating file with static data
#    createJSON (static_data, paste(destdir,"/scm-static.json", sep=''))

    pass

def tsData(period, startdate, enddate, idb, destdir, granularity, conf):
#    evol_data = GetSCMEvolutionaryData(period, conf$startdate, conf$enddate, conf$identities_db)
#
#    if ('companies' %in% reports) { 
#        companies <- EvolCompanies(period, conf$startdate, conf$enddate)
#        evol_data = merge(evol_data, companies, all = TRUE)
#    }
#    if ('countries' %in% reports) {
#        countries <- EvolCountries(period, conf$startdate, conf$enddate)
#        evol_data = merge(evol_data, countries, all = TRUE)
#    }
#    if ('domains' %in% reports) {
#        domains <- EvolDomains(period, conf$startdate, conf$enddate)
#        evol_data = merge(evol_data, domains, all = TRUE)
#    }
#
#    evol_data <- completePeriodIds(evol_data, conf$granularity, conf)
#    evol_data <- evol_data[order(evol_data$id), ]
#    evol_data[is.na(evol_data)] <- 0
#
#    # 3- Creating a JSON file 
#    createJSON (evol_data, destdir+"/scm-evolutionary.json")
    pass

def peopleData(period, startdate, enddate, idb, destdir):
#    all.top.authors <- top_authors_data[['authors.']]$id
#    all.top.authors <- append(all.top.authors, top_authors_data[['authors.last year']]$id)
#    all.top.authors <- append(all.top.authors, top_authors_data[['authors.last month']]$id)
#    all.top.authors <- unique(all.top.authors)
#    createJSON(all.top.authors, paste(destdir,"/scm-people.json", sep=''))
#
#    for (upeople_id in all.top.authors) {
#        evol_data <- GetEvolPeopleSCM(upeople_id, period, 
#                conf$startdate, conf$enddate)
#        evol_data <- completePeriodIds(evol_data, conf$granularity, conf)
#        evol_data[is.na(evol_data)] <- 0
#        createJSON (evol_data, paste(destdir,"/people-",
#                        upeople_id,"-scm-evolutionary.json", sep=''))
#        static_data <- GetStaticPeopleSCM(upeople_id, 
#                conf$startdate, conf$enddate)
#        createJSON (static_data, paste(destdir,"/people-",
#                        upeople_id,"-scm-static.json", sep=''))
#    }

    pass

def reposData(period, startdate, enddate, idb, destdir, conf):
#    repos  <- repos_name(conf$startdate, conf$enddate)
#    repos <- repos$name
#    createJSON(repos, paste(destdir,"/scm-repos.json", sep=''))
#
#    for (repo in repos) {
#        repo_name = paste("'", repo, "'", sep='')
#        repo_aux = paste("", repo, "", sep='')
#        print (repo_name)
#
#        evol_data = GetSCMEvolutionaryData(period, conf$startdate, conf$enddate, conf$identities_db, list("repository", repo_name))
#        evol_data <- completePeriodIds(evol_data, conf$granularity, conf)
#        evol_data <- evol_data[order(evol_data$id), ]
#        evol_data[is.na(evol_data)] <- 0
#
#        createJSON(evol_data, paste(destdir, "/",repo_aux,"-scm-rep-evolutionary.json", sep=''))
#
#        static_data = GetSCMStaticData(period, conf$startdate, conf$enddate, conf$identities_db, list("repository", repo_name))
#
#        createJSON(static_data, paste(destdir, "/",repo_aux,"-scm-rep-static.json", sep=''))        
#    }
    pass

def companiesData(period, startdate, enddate, idb, destdir):
#    companies  <- companies_name_wo_affs(c("-Bot", "-Individual", "-Unknown"), conf$startdate, conf$enddate)
#    companies <- companies$name
#    createJSON(companies, paste(destdir,"/scm-companies.json", sep=''))
#
#    for (company in companies){
#        company_name = paste("'", company, "'", sep='')
#        company_aux = paste("", company, "", sep='')
#        print (company_name)
#
#        ######
#        #Evolutionary data per company
#        ######    
#        # 1- Retrieving and merging info  
#        evol_data = GetSCMEvolutionaryData(period, conf$startdate, conf$enddate, conf$identities_db, list("company", company_name))
#
#        evol_data <- completePeriodIds(evol_data, conf$granularity, conf)
#        evol_data <- evol_data[order(evol_data$id), ]
#        evol_data[is.na(evol_data)] <- 0
#
#        # 2- Creation of JSON file
#        createJSON(evol_data, paste(destdir,"/",company_aux,"-scm-com-evolutionary.json", sep=''))
#
#        ########
#        #Static data per company
#        ########
#        static_data <- GetSCMStaticData(period, conf$startdate, conf$enddate, conf$identities_db, list("company", company_name))
#
#        createJSON(static_data, paste(destdir,"/",company_aux,"-scm-com-static.json", sep=''))
#
#        top_authors <- company_top_authors(company_name, conf$startdate, conf$enddate)
#        createJSON(top_authors, paste(destdir,"/",company_aux,"-scm-com-top-authors.json", sep=''))
#        top_authors_2006 <- company_top_authors_year(company_name, 2006)
#        createJSON(top_authors_2006, paste(destdir,"/",company_aux,"-scm-top-authors_2006.json", sep=''))
#        top_authors_2009 <- company_top_authors_year(company_name, 2009)
#        createJSON(top_authors_2009, paste(destdir,"/",company_aux,"-scm-top-authors_2009.json", sep=''))
#        top_authors_2012 <- company_top_authors_year(company_name, 2012)
#        createJSON(top_authors_2012, paste(destdir,"/",company_aux,"-scm-top-authors_2012.json", sep=''))    
#    }
    pass

def countriesData(period, startdate, enddate, idb, destdir):
#    countries  <- scm_countries_names(conf$identities_db,conf$startdate, conf$enddate)
#    countries <- countries$name
#    createJSON(countries, paste(destdir,"/scm-countries.json", sep=''))
#
#    for (country in countries) {
#        if (is.na(country)) next
#        print (country)
#        country_name = paste("'", country, "'", sep='')
#
#        evol_data = GetSCMEvolutionaryData(period, conf$startdate, conf$enddate, conf$identities_db, list("country", country_name))
#        # evol_data <- EvolCommits(period, conf$startdate, conf$enddate, conf$identities_db, country=country_name)
#        evol_data <- completePeriodIds(evol_data, conf$granularity, conf)
#        # evol_data <- evol_data[order(evol_data$id), ]
#        # evol_data[is.na(evol_data)] <- 0
#
#        createJSON (evol_data, paste(destdir, "/",country,"-scm-cou-evolutionary.json",sep=''))
#
#        # data <- scm_countries_static(conf$identities_db, country, conf$startdate, conf$enddate)
#        static_data = GetSCMStaticData(period, conf$startdate, conf$enddate, conf$identities_db, list("country", country_name))
#        createJSON (static_data, paste(destdir, "/",country,"-scm-cou-static.json",sep=''))
#    }

    pass

def domainsData(period, startdate, enddate, idb, destdir):
#    domains <- scm_domains_names(conf$identities_db,conf$startdate, conf$enddate)
#    domains <- domains$name
#    createJSON(domains, paste(destdir,"/scm-domains.json", sep=''))
#
#    for (domain in domains) {
#        domain_name = paste("'", domain, "'", sep='')
#        domain_aux = paste("", domain, "", sep='')
#        print (domain_name)

#        evol_data = GetSCMEvolutionaryData(period, conf$startdate, conf$enddate, conf$identities_db, list("domain", domain_name))
#        evol_data <- completePeriodIds(evol_data, conf$granularity, conf)
#        evol_data <- evol_data[order(evol_data$id), ]
#        evol_data[is.na(evol_data)] <- 0
#
#        createJSON(evol_data, paste(destdir, "/", domain_aux,"-scm-dom-evolutionary.json", sep=''))
#
#        static_data = GetSCMStaticData(period, conf$startdate, conf$enddate, conf$identities_db, list("domain", domain_name))
#
#        createJSON(static_data, paste(destdir, "/", domain_aux, "-scm-dom-static.json", sep=''))
#    }
    pass


def companies_countriesData(period, startdate, enddate, idb, destdir):
#    companies  <- companies_name(conf$startdate, conf$enddate)
#    companies <- companies$name
#    for (company in companies){
#        countries  <- scm_countries_names(conf$identities_db,conf$startdate, conf$enddate)
#    countries <- countries$name
#    for (country in countries) {
#            company_name = paste(c("'", company, "'"), collapse='')
#            company_aux = paste(c("", company, ""), collapse='')
#
#            ###########
#            if (is.na(country)) next
#            print (paste(country, "<->", company))
#            data <- scm_companies_countries_evol(conf$identities_db, company, country, nperiod, conf$startdate, conf$enddate)
#            if (length(data) == 0) {
#                data <- data.frame(id=numeric(0),commits=numeric(0),authors=numeric(0))
#            }
#
#            data = completeZeroPeriod(data, nperiod, conf$str_startdate, conf$str_enddate)
#            data$week <- as.Date(conf$str_startdate) + data$id * nperiod
#            data$date  <- toTextDate(GetYear(data$week), GetMonth(data$week)+1)
#            data <- data[order(data$id), ]
#            createJSON (data, paste("data/json/companycountry/",company,".",country,"-scm-evolutionary.json",sep=''))
#
#            data <- scm_countries_static(conf$identities_db, country, conf$startdate, conf$enddate)
#            createJSON (data, paste("data/json/companycountry/",company,".",country,"-scm-static.json",sep=''))
#
#            #################
#
#
#        }
#    }
    pass


def topData(period, startdate, enddate, idb, destdir, bots):
#    top_authors_data <- top_authors(conf$startdate, conf$enddate)
#    top_authors_data <- list()
#    top_authors_data[['authors.']] <- top_people(0, conf$startdate, conf$enddate, "author" , "" )
#    top_authors_data[['authors.last year']]<- top_people(365, conf$startdate, conf$enddate, "author", "")
#    top_authors_data[['authors.last month']]<- top_people(31, conf$startdate, conf$enddate, "author", "")
#    createJSON (top_authors_data, paste(destdir,"/scm-top.json", sep=''))
#    
#    # Top files
#    top_files_modified_data = top_files_modified()
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
    logging.info("Starting MLS data source analysis")
    opts = read_options()
    period = getPeriod(opts.granularity)
    reports = opts.reports.split(",")
    # filtered bots

    bots = ["-Bot", "-Individual", "-Unknown"]
    # TODO: hack because VizR library needs. Fix in lib in future
    startdate = "'"+opts.startdate+"'"
    enddate = "'"+opts.enddate+"'"

    # Working at the same time with VizR and VizPy yet
    vizr.SetDBChannel (database=opts.dbname, user=opts.dbuser, password=opts.dbpassword)
    # GrimoireSQL.SetDBChannel (database=opts.dbname, user=opts.dbuser, password=opts.dbpassword)

    tsData (period, startdate, enddate, opts.identities_db, opts.destdir, opts.granularity, opts)
    aggData(period, startdate, enddate, opts.identities_db, opts.destdir)

    if ('people' in reports):
        peopleData (period, startdate, enddate, opts.identities_db, opts.destdir)
    if ('repositories' in reports):
        reposData (period, startdate, enddate, opts.identities_db, opts.destdir, opts)
    if ('countries' in reports):
        countriesData (period, startdate, enddate, opts.identities_db, opts.destdir)
    if ('companies' in reports):
        companiesData (period, startdate, enddate, opts.identities_db, opts.destdir)
    if ('companies-countries' in reports):
        companies_countriesData (period, startdate, enddate, opts.identities_db, opts.destdir)

    topData(period, startdate, enddate, opts.identities_db, opts.destdir, bots)