import tweepy
from tweepy import OAuthHandler
import json
import pandas as pd
from datetime import datetime
from datetime import timedelta
from dateutil import parser
import cmath
import math
from math import log
import numpy as np
import boto3
import boto

import collections
from collections import Counter

import gensim
import pkgutil

modules = pkgutil.iter_modules(gensim.__path__)
for module in modules:
    print(module[1])

from nltk.stem.wordnet import WordNetLemmatizer

lem = WordNetLemmatizer()

from nltk.stem.porter import *

stemmer = PorterStemmer()

import nltk

nltk.download('all')

from sklearn.datasets import fetch_20newsgroups

newsgroups_train = fetch_20newsgroups(subset='train', shuffle=True)
newsgroups_test = fetch_20newsgroups(subset='test', shuffle=True)

import gensim
import pkgutil

modules = pkgutil.iter_modules(gensim.__path__)
for module in modules:
    print(module[1])

from nltk.stem.wordnet import WordNetLemmatizer

lem = WordNetLemmatizer()

from nltk.stem.porter import *

stemmer = PorterStemmer()

import collections
from collections import Counter

consumer_key = 'PQzx2JmWS3kxFCZ4vjHp3SzCI'
consumer_secret = 'YFJs8IJKj0Sx9gjSIxxeUAuOa0tPoYHmLw51p8mRFtyxafF5aA'
access_token = '838007462817071105-KccYqMF5PcZo0XqH0HGIUeqwlYkeJjy'
access_secret = 'ZD90hvLFwDCYY93dmFMRYlfSoukb33h5TgJTh7O9kDwv9'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

keywords = ["Donald Trump", "US Elections", "Steven mnuchin", "Dollar", "Treasury", "IMF", "US GDP", "US Economy",
            "US Exports", "US UnEmployment"]

print(len(keywords))

message, valid_data, ML_re, ML_req, Gmessage, collect, list_of_imp_words, favorite_count, tweet_count, retweet_count, created_at, user_name, screen_name, verified, followers_count, following_count, days, days_since_last_Tweet, no_of_tweets, no_of_his_own_tweets, retweet_count_of_his_posts, favorite_count_of_his_posts, last_tweet_date = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

for keyword in range(len(keywords)):

    tweets = tweepy.Cursor(api.search, q=keywords[keyword] + "-filter:retweets", lang='en'
                           # since="2019-09-19",
                           # until="2019-09-20"
                           ).items(298)

    today = datetime.now()
    DD = timedelta(days=30)
    earlier = today - DD
    earlier_str = earlier.strftime("%Y-%m-%d %H:%M:%S")

    endDate = datetime(2019, 9, 20)
    count = 0
    lol = 1

    wordsss = ["Interest Rate", "Investment", "jobs", "smallbiz", "marketing", "networking", "socialmedia", "tax",
               "smallbusinesssaturday", "smallbizsat", "sensex", "shoplocal", "startups", "innovation", "restaurant",
               "socialbiz", "socialbusiness", "mobile", "socbiz", "management", "ecommerce", "homebiz", "homebusiness",
               "smallbusiness", "External capital", "Cash outflow", "entrepreneurs", "Revenue", "Profit", "Loss",
               "Recession", "Debt", "Collateral", "Mortgage", "Short-term loan", "Loan", "Long-term loan",
               "Credit rating", "Overdraft", "Shares", "Stocks", "Rally", "Bull market", "Bear market", "economics",
               "fund", "banking", "bank", "business", "investment", "corporate finance", "credit", "banker", "treasury",
               "portfolio", "short", "investments", "financial", "capital structure", "management", "financing",
               "fiscal", "funds", "monetary", "asset", "investing", "bankroll", "equity", "money", "real estate",
               "minister", "public finance", "cash", "government", "commerce", "personal finance", "agriculture",
               "affairs", "repayment", "planning", "deputy", "tax", "sector", "vice", "loans", "executive",
               "accounting", "debt", "treasurer", "taxation", "RELATED WORDS CONTINUE AFTER ADVERTISEMENT",
               "venture capital", "cash in hand", "capital", "liability", "quaestor", "direction", "flotation",
               "funding", "back", "pay", "seed", "refinance", "long", "accumulation", "insurance", "retirement",
               "stock", "lender", "creditor", "moneylender", "floatation", "bond", "financial engineering", "payout",
               "depositor", "banklike", "foreign", "loan", "ach", "inventory", "currency", "banc", "debtor", "banco",
               "dollar", "cabinet", "coiner", "managing", "boodle", "wallet", "moneyback", "subsidization", "reform",
               "budget", "imf", "nonbank", "economic", "teller", "banknote", "policy", "ministers", "stock market",
               "ministry", "moneywise", "grubstake", "office", "pecuniary", "prime", "reforms", "secretary", "bankable",
               "administration", "economy", "industry", "chief", "commission", "chairman", "cybermoney", "labor",
               "coinage", "cent", "cashless", "setoff", "dollarless", "bankers", "institutional", "plan", "banks",
               "plans", "proposed", "adviser", "premier", "time value of money", "levy", "meanwhile", "firms",
               "imburse", "antimoney", "committee", "governments", "trade", "proposals", "interest", "portfolios",
               "senior", "reimburse", "rate of return", "cashola", "moola", "policies", "fundraiser", "dollarwise",
               "rainmaker", "institutions", "development", "nomisma", "announced", "spending", "ducat", "privatization",
               "agreed", "federal", "mitre", "key", "advisor", "bailout", "exchequer", "current", "restructuring",
               "private", "cyberbanking", "penny", "domestic", "suggested", "package", "defence", "meeting",
               "narcodollar", "thrift", "board", "pledged", "general", "health", "promised", "economist", "discuss",
               "welfare", "moneymaker", "ministries", "oversees", "billfold", "pinchpenny", "guilder", "usurer",
               "nummary", "wall street", "pokédollar", "investor", "modaraba", "dime", "coinless", "purse", "coin",
               "london stock exchange", "bagman", "cyberbank", "durable good", "appropriation", "shekel", "volatility",
               "megadollar", "political economy", "business enterprise", "economic science", "capital account",
               "high finance", "commercial enterprise", "sheqel", "loonie", "moneyboy", "pickpurse", "monetize",
               "inflation", "theorica", "streambank", "mutual fund", "hedge", "databank", "prestation", "mintmaster",
               "eurodollar", "embank", "capital budgeting", "cyberwallet", "mitsuzuka", "business valuation",
               "real options valuation", "central bank", "financial institution", "money supply", "spillionaire",
               "bank rate", "initial public offering", "oysterbank", "bridge loan", "cash advance", "caution money",
               "store money", "liquid asset", "cash flow", "depository financial institution", "charge interest",
               "credit transfer", "working capital", "e bank", "in bank", "money holder", "dollar bill", "blind ecash",
               "e money", "peace dividend", "keep money", "seed money", "fiat money", "in wallet", "cheque book cover",
               "working capital management", "rent money", "plastic money", "ready money", "piggy bank", "dirty money",
               "fold money", "penny pincher", "cash management", "cash on barrelhead", "paper bill", "front money",
               "mortgage lender", "monetary instrument", "hard money", "bank cheque", "dead president", "bank card",
               "food bank", "break bank", "paper money", "in cash", "medium of exchange", "investment management",
               "hong kong dollar", "penny pinch", "line of credit", "accountancy", "securitization", "lending",
               "budgeting", "borrowing", "mortgage", "financier", "macroeconomics", "refinancing", "lenders",
               "bookkeeping", "marketing", "underwriting", "auditor", "liquidity", "communications", "mergers",
               "dead pledge", "structuring", "accountant", "leasing", "entrepreneurship", "transportation",
               "procurement", "auditing", "governance", "bonds", "indebtedness", "engineering", "kpmg", "broking",
               "agribusiness", "microeconomics", "securities", "telecommunications", "logistics", "infrastructure",
               "disbursements", "income", "brokerage", "tenens", "healthcare", "aviation", "fundraising", "blood money",
               "operate expense", "money changer", "money of account", "pay for something", "affinity card", "at bank",
               "smart money", "tax collector", "accounting profession", "cash bill", "hold money", "banker's lien",
               "lubrication payment", "unemployment benefit", "money change", "financial accounting", "grease payment",
               "legal tender", "war chest", "debit card", "half dollar", "premium bond", "blow one's wad",
               "financial risk management", "payment counter", "money chest", "key money", "deep pocket",
               "maundy money", "economic value", "save bank", "variable", "bank account", "nickel and dime",
               "account book", "cash coin", "small change", "price", "coin purse", "common purse", "cha ching",
               "carry money", "financial instrument", "cash up", "pay for", "monetary unit", "financial risk",
               "pretty penny", "mathematics", "credit risk", "checkbook holder", "monopoly money", "new penny",
               "pay out", "cash cow", "checkbook cover", "in purse", "market risk", "put aside", "hard up",
               "forfaiting", "controllership", "receivables", "mortage", "financer", "corporative", "diba",
               "undercapitalization", "euromoney", "foreign exchange risk", "world bank", "for profit",
               "third party processor", "pay one's due", "credit union", "your pocket", "hot money", "liquidity risk",
               "risk management", "basel accords", "financial intermediary", "bond market", "certainty", "statistics",
               "derivative", "financial market", "business management", "equity financing", "institutional investor",
               "pension fund", "private investors", "federal reserve system", "united states", "monetary resource",
               "pecuniary resource", "investment banker", "internal audit", "gross profit margin", "hire purchase",
               "fannie mae", "chartered accountant", "vice president", "money laundering",
               "accounts receivable financing", "managing director", "credit foncier", "bank of england",
               "united kingdom", "lender of last resort", "efficient-market hypothesis", "interest rate",
               "goods and services", "real vs. nominal in economics", "economic model", "financial model",
               "homo economicus", "rational pricing", "modern portfolio theory", "capital asset pricing model",
               "black–scholes model", "valuation of options", "fisher separation theorem",
               "the theory of investment value", "experimental finance", "vernon l. smith",
               "journal of behavioral finance", "gunduz caginalp", "quantitative behavioral finance",
               "behavioral finance", "financial econometrics", "actuarial science", "professional qualification",
               "quantitative analyst", "computational finance", "numerical analysis", "mathematical model",
               "mathematical finance", "applied mathematics", "modigliani–miller theorem", "jurisdiction",
               "shareholder", "public limited company", "management", "stock exchange", "asset", "manufacturing",
               "product", "company", "listing", "corporation", "italians", "investor", "creditor", "accountant",
               "investments", "liability", "business name", "limited liability", "corporate tax", "merchandise",
               "machine", "tool", "offshore financial center", "handicraft", "offshore company",
               "segregated portfolio company", "industry", "privately held company", "advertising", "listing rules",
               "pricing", "parent company", "economic entity", "insurance", "luca pacioli", "finance", "marketing",
               "regulatory agency", "rate of return", "public finance", "corporate finance", "personal finance",
               "wage labour", "broker", "high tech manufacturing", "raw material", "finished good", "broadcasting",
               "american marketing association", "aviation", "capital", "security", "digital marketing",
               "business operations", "wage", "employment", "treaty", "trademark", "copyright", "patent", "nasdaq",
               "organizational studies", "strategic management", "operations management", "service management",
               "information technology management", "people's republic of china", "state-owned enterprise",
               "commercial law", "legal liability", "code of hammurabi", "freight transport", "maurya empire",
               "health and safety executive", "trade union", "public utility", "initial public offering",
               "shanghai stock exchange", "intellectual property", "hong kong stock exchange",
               "new york stock exchange", "occupational safety and health", "trade secret", "london stock exchange",
               "working conditions", "labour and employment law", "collective bargaining", "tokyo stock exchange",
               "bombay stock exchange", "singapore exchange", "asset", "finance", "investing", "interest", "financial",
               "business", "bank", "venture", "portfolio", "invest", "arbitrage", "fund", "investor", "speculation",
               "diversification", "capital", "acquisitions", "income", "risk", "management", "assets", "rate of return",
               "investment funds", "stock", "investiture", "profit", "share", "equity", "commitment", "invested",
               "investors", "financing", "growth", "development", "hedge", "banking", "money", "sector", "firms",
               "trade", "revenue", "securities", "mutual", "market", "insurance", "companies", "shareholder",
               "economic", "profits", "brokerage", "holdings", "debt", "buy into", "expenditure", "outlay",
               "hedge fund", "mutual fund", "time", "dividend", "venture capital", "grooming", "dressing", "promotion",
               "skin", "pay", "yield", "cutis", "pellicle", "subscribe", "pyramid", "bull", "bear", "leveraging",
               "leverage", "investments", "warren buffett", "funds", "tegument", "committedness", "banks", "credit",
               "statistics", "managing", "corporate", "institutional", "enterprises", "firm", "markets", "ventures",
               "global", "partners", "value", "capital expenditure", "businesses", "savings", "raise", "lending",
               "trust", "boost", "equities", "exchange", "expand", "industry", "loans", "domestic", "resources",
               "private", "corporations", "acquisition", "benefit", "trading", "diversified", "projects", "citigroup",
               "expects", "sachs", "revenues", "billion", "commodity", "sectors", "company", "dollar", "overseas",
               "deals", "bankers", "estate", "managers", "currency", "costs", "increase", "buying", "retail",
               "commerce", "dollars", "purchasing", "expanding", "merrill", "capital gain", "saving",
               "foreign direct investment", "forbes", "government bond", "emerging markets", "reinvestment", "invests",
               "capitalization", "investment strategy", "wealth", "employment", "intermediary", "funding", "chemise",
               "outfit", "spending", "bullion", "merchant", "contribution", "involvement", "placements", "vest",
               "participation", "inverter", "payback", "placement", "lender", "fiscal", "fostering", "input", "buck",
               "equipage", "caftan", "reversal", "effort", "costume", "robe", "dress", "vesture", "jerkin", "attire",
               "apparel", "care", "waistcoat", "garment", "custody", "roi", "kirtle", "reverse", "confinement",
               "remand", "undershirt", "reversed", "loan", "refund", "placing", "modiste", "frock", "gown", "mortgage",
               "repayment", "reimburse", "capitalize", "internment", "tog", "dressmaker", "fdi", "institutionalization",
               "aum", "profitability", "securitization", "rockport", "liquidity", "valuation", "infrastructure", "reit",
               "greenfield", "refinancing", "structuring", "blouse", "clothe", "payment", "mantua", "plainclothes",
               "raiment", "payout", "kimono", "sleeveless", "garb", "surety", "deposit", "petticoat", "undergarment",
               "vestment", "wear", "overall", "expend", "skirt", "moneylender", "shirt", "swimsuit", "wearer",
               "pinafore", "remittance", "lucre", "bankroll", "accouter", "housedress", "leatherwear", "innerwear",
               "bank deposit", "strapless", "overdress", "dressable", "costumal", "prestation", "coatdress",
               "nominal value", "shirtdress", "aguise", "minidress", "economics", "businesswear", "dirndl", "sundress",
               "underdress", "lavalava", "outerwear", "pinny", "dizen", "slutwear", "grubstake", "simar",
               "investissement", "ofdi", "sicav", "sinopia", "reim", "shareholdings", "seamark", "forfaiting",
               "overtrading", "stockmarket", "omers", "overwear", "surfwear", "pridewear", "divewear", "unwearable",
               "athleticwear", "moneymaker", "promwear", "bedrape", "coverall", "geekwear", "primp", "monetize",
               "caparison", "reclothe", "clubwear", "beachwear", "dandify", "fetishwear", "clothesless", "nightwear",
               "modaraba", "ravewear", "neckline", "enclothe", "vestiary", "vestiment", "stockingfoot", "vestiture",
               "loungewear", "netherwear", "designerwear", "forbes 400", "due diligence", "earnings per share",
               "edward o. thorp", "consumption", "money belt", "kelly criterion", "google", "volatility", "microsoft",
               "earnings", "mortgage lender", "brokerage firm", "key money", "dead pledge", "liquid asset", "rig out",
               "investment trust", "peace dividend", "fancy dress", "girl clothe", "dress down", "woman clothe",
               "female clothe", "slide fastener", "unit trust", "premium bond", "ao dai", "cocktail dress",
               "mother hubbard", "break bank", "women's clothe", "blood money", "pay for", "fnance and economy",
               "clothe topic", "cash in hand", "dress rehearsal", "hussy up", "french dress", "protective garment",
               "cross dress", "slip on", "item of clothe", "ready money", "ball gown", "institutional investors",
               "real estate", "balanced fund", "front money", "form of clothe", "caution money", "seed money",
               "doll up", "salad cream", "double denim", "ready to wear", "bundle up", "piece of clothe",
               "thousand island dress", "pay out", "dress gown", "credit transfer", "dollar cost averaging",
               "woman's clothe", "stark bollock naked", "morning dress", "operate expense", "amazon.com", "clothe item",
               "man's clothe", "smock frock", "rent money", "street clothe", "princesse dress", "penny pinch",
               "banker's lien", "outer wear", "market timing", "civilian clothe", "capital gain tax", "swim costume",
               "bridge loan", "medium of exchange", "dollar bill", "pay one's due", "tank top", "work clothe",
               "lump sum", "code of hammurabi", "benjamin graham", "david dodd", "security analysis",
               "wall street crash of 1929", "price to earnings ratio", "price-to-book ratio", "free cash flow",
               "earnings before interest, taxes, depreciation and amortization", "working capital", "capital structure",
               "debt-to-equity ratio", "mergers and acquisitions", "economics", "economic", "saving", "sector",
               "demand", "currency", "inflation", "finance", "goods", "financial", "gdp", "trade", "production",
               "consumption", "thriftiness", "barter", "distribution", "economic system", "market economy", "service",
               "good", "growth", "recession", "slowing", "recovery", "market", "downturn", "slowdown", "unemployment",
               "crisis", "economist", "markets", "global", "consumer", "prices", "outlook", "weakening", "exports",
               "country", "fiscal", "nation", "competitiveness", "sentiment", "protectionism", "globalization",
               "real versus nominal value", "agriculture", "infrastructure", "capitalism", "trading", "service sector",
               "technology", "innovation", "economical", "supply", "system", "scheme", "industrialism", "efficiency",
               "frugality", "retrenchment", "downsizing", "curtailment", "action", "credit", "debit", "value",
               "economize", "thrifty", "sociology", "saver", "history", "save", "anthropology", "frugal", "geography",
               "frugalness", "economically", "economies", "europe", "sluggish", "rise", "conservation", "weak",
               "rising", "domestic", "spending", "engineering", "stronger", "conserve", "trend", "boost", "low-carbon",
               "management", "confidence", "decline", "growing", "rapidly", "dramatically", "industry", "impact",
               "poor", "emerging", "expectations", "robust", "shrinking", "slow", "profession", "steady", "worries",
               "improving", "surplus", "turmoil", "falling", "pushed", "prospects", "fall", "partly", "declining",
               "slump", "accelerating", "interest", "sectors", "balance", "stability", "productivity", "increase",
               "weaker", "rates", "worried", "concern", "concerns", "ease", "driven", "pushing", "slowed", "expanding",
               "stabilize", "reforms", "rate", "industrial", "sees", "borrowing", "struggling", "steadily", "strong",
               "worse", "forecast", "deficit", "predicted", "decade", "woes", "change", "sharply", "conservator",
               "increasing", "current", "worsening", "economizer", "analysts", "investment", "autosave", "preservation",
               "preserve", "keep", "industrial relations", "keeper", "child labor", "sumer",
               "universal access to education", "market-based economy", "babylonians", "retain", "safeguard", "defend",
               "bergh", "debt", "savior", "defender", "guardian", "preserver", "mixed economy", "black economy",
               "free enterprise", "laissez-faire economy", "private enterprise", "state socialism",
               "non-market economy", "state capitalism", "economy of scale", "shekel", "medium of exchange", "rescue",
               "mesopotamia", "protect", "barley", "retention", "metric", "savepoint", "maintenance", "thrift",
               "beekeeping", "donjon", "guard", "planned economy", "withhold", "keepsies", "preservable",
               "green economy", "safe", "savefile", "freeholder", "maintain", "bodyguard", "keepable", "protector",
               "social science", "scarcity", "eco", "medieval", "miskeep", "ward", "upholder", "maintainable",
               "underkeep", "protective", "ransom", "economic sociology", "chaperone", "capital", "defensative",
               "defendable", "economic history", "defence", "enshield", "economic anthropology", "exception",
               "safekeeping", "overkeep", "bank", "cautious", "guardianship", "economic geography", "custodian",
               "protectable", "marmalade", "overprotect", "stronghold", "prudence", "expenditure", "security", "wary",
               "beshield", "keepalive", "sentinel", "company", "protection", "salvage", "prudent", "banc",
               "goods and services", "beward", "foreguard", "stockholder", "custody", "vindicate", "reservatory",
               "defense", "antwerpen", "fund", "jailer", "convoy", "custodial", "uphold", "wite", "shield",
               "business administration", "circumspect", "asset", "defensive", "safeness", "precaution",
               "applied science", "treasury", "colonies", "apologist", "hoard", "conservancy", "redemption", "immune",
               "retainer", "chary", "preservative", "spain", "caretaker", "cautiously", "maintainer", "reservation",
               "spare", "wariness", "economic agent", "except", "portugal", "expendable", "economists", "prosperity",
               "tourism", "finances", "incomes", "businesses", "housing", "contraction", "government", "employment",
               "industries", "jobs", "upturn", "stimulus", "deflation", "business", "policymakers", "stagnation",
               "society", "climate", "eurozone", "greenback", "polity", "macroeconomics", "bankruptcies", "banks",
               "exporters", "hyperinflation", "dollar", "entrepreneurship", "workforce", "deceleration", "fisc",
               "democracy", "auto", "population", "upswing", "marketplace", "commerce", "environment", "devaluation",
               "france", "environmentalism", "environmentalist", "embank", "quicksave", "tutelage", "omnium",
               "netherlands", "prophylactic", "enshrine", "carefulness", "lifeguard", "accumulation",
               "primary sector of the economy", "secondary sector of the economy", "merchant",
               "tertiary sector of the economy", "life save", "secularization", "housekeep", "nobles", "degrowth",
               "confiture", "watchkeeping", "real gdp", "radioprotection", "bankers", "english language", "keep off",
               "stormproof", "ancient greek", "citizens", "actively protect", "nation-state", "keep from",
               "commodity money", "fixative", "watch over", "grubstake", "keep up", "rrsp", "city states",
               "deindustrialization", "stagflation", "swonk", "econ", "disinflation", "sacci", "decine", "stockmarket",
               "pocketbooks", "decarbonise", "reflation", "downspin", "chier", "dollarization", "pinchpenny", "product",
               "withholder", "bankroll", "freegan", "barkeeping", "subsistence farming", "competition",
               "nature preserve", "keep it up", "body guard", "anthropological", "put aside", "hold over", "keep away",
               "ancient greece", "keep in", "bond slaves", "baby sit", "shoot preserve", "manufacturing",
               "on defensive", "mining", "save game", "social groups", "nature reserve", "transport", "venture capital",
               "physiocracy", "new world", "ward off", "jakob fugger", "world", "giovanni di bicci de' medici",
               "put by", "mercantilism", "postmodernism", "internet", "home", "neoliberalism", "marco polo",
               "safe haven", "mutual fund", "christopher columbus", "keep faith", "vasco da gama", "security guard",
               "nest egg", "peace dividend", "plan economy", "keep back", "keep go", "keep up with", "mortgage lender",
               "salt away", "stock exchange", "world bank", "private sector", "prison guard", "save account",
               "store away", "keep in mind", "keep straight", "fight inflation", "penny pincher", "take care",
               "keep be", "fail safe", "earn one's keep", "unemployment rate", "credit crunch", "disposable income",
               "inflationary spiral", "pump priming", "monetary policy", "central bank", "weimar republic",
               "body politic", "muddle through", "durable goods", "leading indicator", "lagging indicator",
               "earnest money", "division of labor", "financial institution", "great britain", "guard dog", "bank rate",
               "caution money", "keynesianism", "wirtschaftswunder", "free trade", "custom duties", "public interest",
               "secretaries of state", "amschel mayer rothschild", "industrial revolution", "adam smith",
               "national economy", "natural price", "supply and demand", "thomas malthus", "human overpopulation",
               "greek language", "united kingdom", "north america", "mass production", "black market",
               "great depression", "bill clinton", "world war", "developing countries", "economic growth",
               "friedrich august von hayek", "gross national product", "john maynard keynes", "revolutions of 1989",
               "gdp per capita", "social market economy", "affluent society", "three-sector theory",
               "john kenneth galbraith", "mass consumption economy", "milton friedman"]


    def lemmatize_stemming(text):
        return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


    # Tokenize and lemmatize
    wordss = []


    def preprocess(text):
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                wordss.append(lemmatize_stemming(token))
        return wordss


    for p in range(len(wordsss)):
        preprocess(wordsss[p])

    final_wordss = []
    for num in wordss:
        if num not in final_wordss:
            final_wordss.append(num)

    """        def lemmatize_stemming(message):
                return stemmer.stem(WordNetLemmatizer().lemmatize(message, pos='v'))        
            for token in gensim.utils.simple_preprocess(tweet.text) :
                if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                    tlmessage.append(lemmatize_stemming(token))"""

    for tweet in tweets:

        def lemmatize_stemming(text):
            return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

            # Tokenize and lemmatize


        result = []


        def preprocess(text):
            for token in gensim.utils.simple_preprocess(text):
                if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                    result.append(lemmatize_stemming(token))
            return result


        print(preprocess(tweet.text))

        results = []

        result.append('hi')

        results.append(result)

        # print(results)
        # print(final_wordss)

        dictionary = gensim.corpora.Dictionary(results)

        bow_corpus = [dictionary.doc2bow(doc) for doc in results]

        lda_model = gensim.models.LdaMulticore(bow_corpus,
                                               num_topics=2,
                                               id2word=dictionary,
                                               passes=10,
                                               workers=2)

        for idx, topic in lda_model.print_topics(-1):
            # print("Topic: {} \nWords: {}".format(idx, topic ))
            print("\n")

            output = re.sub('[^A-Za-z ]+', '', topic)

            # output = re.sub(r'\d+', '', topic)
            # print (output)

            final_list = output.split()
            # print("final")
            # print(final_list)
            list_of_imp_words.append(final_list)

            countt = 0

            for k in final_wordss:
                for j in range(len(final_list)):
                    if (final_list[j] == k):
                        print(final_list[j])
                        countt = countt + 1

            # print(countt)

            if (countt > 1):

                message.append(tweet.text)
                output = re.sub('[^A-Za-z0-9., ]+', '', tweet.text)
                final_out = re.sub(r'http\S+', '', output)
                Gmessage.append(final_out)
                ML_req.append(final_out.split())
                favorite_count.append(tweet.favorite_count)
                retweet_count.append(tweet.retweet_count)
                created_at.append(tweet.created_at)
                user_name.append(tweet.user.name)
                screen_name.append(tweet.user.screen_name)
                verified.append(tweet.user.verified)
                a = tweet.user.id
                tweet_count.append(api.get_user(a).statuses_count)

                followers_count.append(tweet.user.followers_count)
                following_count.append(tweet.user.friends_count)


                def lemmatize_stemming(text):
                    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


                hello = []
                ML = []
                for token in gensim.utils.simple_preprocess(final_out):
                    if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                        ML.append(token)
                        hello.append(lemmatize_stemming(token))

                collect.append(collections.Counter(hello))
                valid_data.append(hello)
                ML_re.append(ML)
                results = api.user_timeline(id=a, count=1)

                for tweet in results:
                    create = tweet.created_at
                    v = today - create
                    """print(today  )
                    print("my out")
                    print(create )
                    print(v.days)"""
                    days.append(v.days)


                print(lol)
                lol = lol + 1

                new_final_list = []
                for num in message:
                    if num not in new_final_list:
                        new_final_list.append(num)

                a = ({'Message': new_final_list,
                      'valid_data': valid_data,
                      'ML_Required': ML_re,
                      'ML_req': ML_req,
                      'Req Message': Gmessage,
                      'collect': collect,
                      'list_of_imp_words': list_of_imp_words,
                      'Favourite Count': favorite_count,
                      'tweet_count': tweet_count,
                      'Retweet Count': retweet_count,
                      'Created At': created_at,
                      'user_name': user_name,
                      'screen_name': screen_name,
                      'verified': verified,
                      'followers count': followers_count,
                      'following count': following_count,
                      'days': days
                      # 'last20_days':last20_days
                      # 'influence':influence
                      })

                df = pd.DataFrame.from_dict(a, orient='index')

                df.transpose()

                df.to_csv("twitter_sort_1.csv")

                pd.read_csv('twitter_sort_1.csv', header=None).T.to_csv('US Related Data_1.csv', header=False,
                                                                        index=False)

                # df.to_csv("twitter_sort_1.csv")

                # print(df)
                break

df = pd.read_csv('US Related Data_1.csv')

days_since_last_Tweet, no_of_tweets, no_of_his_own_tweets, retweet_count_of_his_posts, favorite_count_of_his_posts, last_tweet_date = [], [], [], [], [], []

for i in range(df.shape[0]):

    tweets = []

    for tweet in api.user_timeline(df["screen_name"][i], count=50):
        tweets.append(tweet)

    userdf = pd.DataFrame([tweet.id for tweet in tweets], columns=['id'])
    userdf['Date of creation'] = [datetime.strptime(str(tweet.created_at), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                                  for tweet in tweets]
    userdf['Re-tweet count'] = [tweet.retweet_count for tweet in tweets]
    userdf['Favorite count'] = [tweet.favorite_count for tweet in tweets]
    userdf['Tweet'] = [tweet.text for tweet in tweets]
    userdf['Re-tweeted'] = [tweet.retweeted for tweet in tweets]
    notweeted = []
    for i in userdf['Tweet']:
        if "RT" not in i:
            notweeted.append(True)
        else:
            notweeted.append(False)
    userdf['Re-tweetedMan'] = notweeted
    userdf['Date of creation'] = userdf['Date of creation'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    present = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), '%Y-%m-%d')
    days_since_last_Tweet.append(userdf["Date of creation"][0])
    no_of_tweets.append(userdf.shape[0])
    no_of_his_own_tweets.append(userdf[userdf["Re-tweetedMan"]].shape[0])
    retweet_count_of_his_posts.append(userdf[userdf["Re-tweetedMan"]]["Re-tweet count"].sum())
    favorite_count_of_his_posts.append(userdf[userdf["Re-tweetedMan"]]["Favorite count"].sum())
    last_tweet_date.append(userdf["Date of creation"][userdf.shape[0] - 1])

df["days_since_last_Tweet"] = days_since_last_Tweet
df["no_of_tweets"] = no_of_tweets
df["no_of_his_own_tweets"] = no_of_his_own_tweets
df["retweet_count_of_his_posts"] = retweet_count_of_his_posts
df["favorite_count_of_his_posts"] = favorite_count_of_his_posts
df["last_tweet_date"] = last_tweet_date
print(df.columns)
df = df.drop(columns=['Unnamed: 0'], axis=1)

df.to_csv('US Related Data_11.csv')

"""
t="finance_data5_2.csv"


bucketName = "test-bucket-saikiran"
Key = t
outPutname = t

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

"""
