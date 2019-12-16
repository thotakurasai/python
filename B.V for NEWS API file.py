!pip install feedparser
!pip install newspaper3k
import feedparser as fp
import json
import csv
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime
import pandas as pd
import numpy as np
import boto3
import boto

from google.colab import files
uploaded = files.upload()

from google.colab import drive
drive.mount('/content/gdrive')

# Install the PyDrive wrapper & import libraries.
# This only needs to be done once in a notebook.
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
# This only needs to be done once in a notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)



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

newsgroups_train = fetch_20newsgroups(subset='train', shuffle = True)
newsgroups_test = fetch_20newsgroups(subset='test', shuffle = True)


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


print(list(newsgroups_train.target_names))

import re

#import substring

lol = 1
z = -1
q = 0

#textt = """Weeks after journalist Jamal Khashoggi's murder inside Saudi Arabia's consulate in Istanbul, the kingdom's crown prince attended the G20 summit in Argentina to an apparent cool reception.During the official family photo, Mohammed bin Salman (MBS), who faced allegations of ordering the October 2, 2018, killing, stood at the far edge of the group portrait. Largely ignored by the leaders of the world's largest economies, he exited the stage quickly afterwards, without stopping to speak to the others. "Saudi Crown Prince sidelined in G20 family photo", "A bro-shake with Putin, a talking-to from Macron: The Saudi prince's less-than-royal treatment at the G-20", read some of the headlines after the November summit.The leaders of France, Canada and the United Kingdom, meanwhile, said they pressed for an investigation into Khashoggi's killing during their separate meetings with Prince Mohammed, who denies any knowledge of the murder.But when the same G20 leaders gathered in Japan's Osaka in June, things appeared different. This time, Prince Mohammed stood front and centre in the family photo, sandwiched between Japanese Prime Minister Shinzo Abe and US President Donald Trump, who at a personal breakfast earlier, congratulated the crown prince for doing a "spectacular job" in "opening up" Saudi Arabia and fighting "terrorism".Remembering Jamal Khashoggi - the prominent Saudi journalist whose 30-year career came to an end when he was killed in the Saudi consulate in Istanbul. pic.twitter.com/zulzY4NrTXThe US president has not been the only leader to have heaped praise on Prince Mohammed over the past year. During a February visit to Pakistan as part of an Asia tour that included stops in China and India, Prince Mohammed was given Pakistan's highest civilian honour after signing investment deals worth $20bn. Meanwhile, Saudi Arabia is scheduled to host next year's G20 summit, and this month it is stepping up preparations for its annual "Davos in the Desert" summit, a high-profile investment conference that last October was shunned by many business leaders amid the global outcry over Khashoggi's murder.  This year, however, business heavy hitters are expected to return to Riyadh, with the list of attendees also reportedly including Jared Kushner, Trump's son-in-law and a senior White House adviser.Riyadh's public relations push has drawn concern from global human rights groups."There is an undeniable risk that with big events scheduled to take place in Saudi Arabia in 2020, such as the G20 summit and the famous Dakar Rally, state-to-state relations could normalise," 19 organisations that include Amnesty International and the Index on Censorship said in a joint statement on Tuesday.The "return of business as usual would mean Khashoggi died in vain", the groups said, "and there is little hope for hundreds of other unlawfully disappeared, detained, tortured or executed activists whose cases failed to attract similar levels of international attention". Bessma Momani, professor of political science at the University of Waterloo in Canada, said world leaders have given Prince Mohammed "a pass", despite incriminating evidence linking him to Khashoggi's killing.She was referring to a June report by a United Nations expert that said it found "credible evidence" warranting further investigation of the crown prince's liability for the killing.The inquiry by Agnes Callamard, UN special rapporteur on extrajudicial killings, said Khashoggi was the victim of "deliberate, premeditated execution" for which Saudi Arabia bore responsibility. Her report backed Turkish intelligence reports that a 15-member hit squad comprising of senior Saudi agents killed and dismembered Khashoggi inside the consulate. Many of Khashoggi's killers were close aides to the crown prince, the inquiry found.  Yet, "not only is he (the crown prince) being welcomed to international events, he continues to have many face-to-face meetings with world leaders, including those from liberal democracies," Momani said.Prince Mohammed's successful comeback bid is a testament to Saudi Arabia's clout on the global stage as the world's top oil producer and arms importer, she added, referring to the kingdom's multibillion-dollar defence contracts with Western countries. Trump, announcing his decision in November last year to "stand with Saudi Arabia", touted Riyadh's import of US weapons, as well as its support of Washington's policies on Iran and Syria.The decision not to take punitive measures against Saudi Arabia for Khashoggi's killing also reflects a rise of "nationalist-populist dictators globally", Momani argued."If you're going to censure Mohammed bin Salman, why wouldn't you censure Xi Jinping of China, who's got one million Muslim Uighurs in internment camps, Narendra Modi of India who's got Muslims in Kashmir in one big open-air prison - so where do you begin the censuring?"In addition to business and geopolitical interests, "there's also an appreciation - whether you like it or not - for some of the economic and social reforms that Mohammed bin Salman has carried out", Momani said, referring to the crown prince's pledge to diversify the Saudi economy away from oil, as well as a decision to grant women the right to drive.Still, the fallout over Khashoggi's murder has cost Prince Mohammed and Saudi Arabia.Germany, Denmark and Finland have banned arms sales to the kingdom, but arguably the most notable effect has been the US Congress's stance towards Riyadh.Despite Trump's fervent support, the Senate in December approved a measure blaming the crown prince for Khashoggi's killing. This year, both the House of Representatives and the Senate voted to end US military support for the Saudi-led war in Yemen - but Trump vetoed those measures.In a Twitter post on Monday, Robert Menendez, a Democratic senator, pledged to continue the effort to hold Saudi Arabia to account.   "Trump has repeatedly vetoed Congress' efforts, but we remain undeterred," he said. "Khashoggi's murder will be remembered as the straw that broke the camel's back - a grim reminder that Saudi behaviour has strayed so far out of line with our own values that business as usual with the kingdom was no longer in our interests," he added in an op-ed for The Washington Post.The disappearance of Saudi journalist #JamalKhashoggi has turned the spotlight on Mohammed bin Salman - whose human rights record casts a dark shadow on his reforms. pic.twitter.com/EwBSJvKjhDAyham Kamel, Middle East director at the Eurasia Group, said the US Congress's stance was among the factors behind Prince Mohammed's recent decision to take responsibility for Khashoggi's killing. In an interview with CBS's 60 minutes programme that aired on Sunday, just as the looming anniversary of Khashoggi's killing began to draw attention to the case, the crown prince denied ordering the murder, but said he took "full responsibility as a leader in Saudi Arabia". The comments "represent a clear shift in approach in embracing the mistake that was made and promising some form of accountability," Kamel said. "He has seen there are limitations to what he can do on the international arena, for sure." However, many have denounced the crown prince's comments. Callamard said they represented an attempt by the crown prince to exonerate himself from direct criminal responsibility in the killing, while The Washington Post's editorial board described them as "a lie that only those wishing to excuse him will accept".Fred Ryan, publisher of the US newspaper, said he believed Khashoggi's case could still be "a turning point".Some actions are too heinous for the public to forget, he wrote in a hopeful op-ed on Sunday. And Khashoggi's murder "might be recorded as the moment when Saudi Arabia began to understand the consequences of its brutality, when the United States learned important lessons about standing up for its values, and when both countries rediscovered liberty, human rights and respect for the truth". """





wordsss=["Interest Rate","Investment","jobs","smallbiz","marketing","networking","socialmedia","tax","smallbusinesssaturday","smallbizsat","sensex","shoplocal","startups","innovation","restaurant","socialbiz","socialbusiness","mobile","socbiz","management","ecommerce","homebiz","homebusiness","smallbusiness","External capital","Cash outflow","entrepreneurs","Revenue","Profit","Loss","Recession","Debt","Collateral","Mortgage","Short-term loan","Loan","Long-term loan","Credit rating","Overdraft","Shares","Stocks","Rally","Bull market","Bear market","economics","fund","banking","bank","business","investment","corporate finance","credit","banker","treasury","portfolio","short","investments","financial","capital structure","management","financing","fiscal","funds","monetary","asset","investing","bankroll","equity","money","real estate","minister","public finance","cash","government","commerce","personal finance","agriculture","affairs","repayment","planning","deputy","tax","sector","vice","loans","executive","accounting","debt","treasurer","taxation","RELATED WORDS CONTINUE AFTER ADVERTISEMENT","venture capital","cash in hand","capital","liability","quaestor","direction","flotation","funding","back","pay","seed","refinance","long","accumulation","insurance","retirement","stock","lender","creditor","moneylender","floatation","bond","financial engineering","payout","depositor","banklike","foreign","loan","ach","inventory","currency","banc","debtor","banco","dollar","cabinet","coiner","managing","boodle","wallet","moneyback","subsidization","reform","budget","imf","nonbank","economic","teller","banknote","policy","ministers","stock market","ministry","moneywise","grubstake","office","pecuniary","prime","reforms","secretary","bankable","administration","economy","industry","chief","commission","chairman","cybermoney","labor","coinage","cent","cashless","setoff","dollarless","bankers","institutional","plan","banks","plans","proposed","adviser","premier","time value of money","levy","meanwhile","firms","imburse","antimoney","committee","governments","trade","proposals","interest","portfolios","senior","reimburse","rate of return","cashola","moola","policies","fundraiser","dollarwise","rainmaker","institutions","development","nomisma","announced","spending","ducat","privatization","agreed","federal","mitre","key","advisor","bailout","exchequer","current","restructuring","private","cyberbanking","penny","domestic","suggested","package","defence","meeting","narcodollar","thrift","board","pledged","general","health","promised","economist","discuss","welfare","moneymaker","ministries","oversees","billfold","pinchpenny","guilder","usurer","nummary","wall street","pokédollar","investor","modaraba","dime","coinless","purse","coin","london stock exchange","bagman","cyberbank","durable good","appropriation","shekel","volatility","megadollar","political economy","business enterprise","economic science","capital account","high finance","commercial enterprise","sheqel","loonie","moneyboy","pickpurse","monetize","inflation","theorica","streambank","mutual fund","hedge","databank","prestation","mintmaster","eurodollar","embank","capital budgeting","cyberwallet","mitsuzuka","business valuation","real options valuation","central bank","financial institution","money supply","spillionaire","bank rate","initial public offering","oysterbank","bridge loan","cash advance","caution money","store money","liquid asset","cash flow","depository financial institution","charge interest","credit transfer","working capital","e bank","in bank","money holder","dollar bill","blind ecash","e money","peace dividend","keep money","seed money","fiat money","in wallet","cheque book cover","working capital management","rent money","plastic money","ready money","piggy bank","dirty money","fold money","penny pincher","cash management","cash on barrelhead","paper bill","front money","mortgage lender","monetary instrument","hard money","bank cheque","dead president","bank card","food bank","break bank","paper money","in cash","medium of exchange","investment management","hong kong dollar","penny pinch","line of credit","accountancy","securitization","lending","budgeting","borrowing","mortgage","financier","macroeconomics","refinancing","lenders","bookkeeping","marketing","underwriting","auditor","liquidity","communications","mergers","dead pledge","structuring","accountant","leasing","entrepreneurship","transportation","procurement","auditing","governance","bonds","indebtedness","engineering","kpmg","broking","agribusiness","microeconomics","securities","telecommunications","logistics","infrastructure","disbursements","income","brokerage","tenens","healthcare","aviation","fundraising","blood money","operate expense","money changer","money of account","pay for something","affinity card","at bank","smart money","tax collector","accounting profession","cash bill","hold money","banker's lien","lubrication payment","unemployment benefit","money change","financial accounting","grease payment","legal tender","war chest","debit card","half dollar","premium bond","blow one's wad","financial risk management","payment counter","money chest","key money","deep pocket","maundy money","economic value","save bank","variable","bank account","nickel and dime","account book","cash coin","small change","price","coin purse","common purse","cha ching","carry money","financial instrument","cash up","pay for","monetary unit","financial risk","pretty penny","mathematics","credit risk","checkbook holder","monopoly money","new penny","pay out","cash cow","checkbook cover","in purse","market risk","put aside","hard up","forfaiting","controllership","receivables","mortage","financer","corporative","diba","undercapitalization","euromoney","foreign exchange risk","world bank","for profit","third party processor","pay one's due","credit union","your pocket","hot money","liquidity risk","risk management","basel accords","financial intermediary","bond market","certainty","statistics","derivative","financial market","business management","equity financing","institutional investor","pension fund","private investors","federal reserve system","united states","monetary resource","pecuniary resource","investment banker","internal audit","gross profit margin","hire purchase","fannie mae","chartered accountant","vice president","money laundering","accounts receivable financing","managing director","credit foncier","bank of england","united kingdom","lender of last resort","efficient-market hypothesis","interest rate","goods and services","real vs. nominal in economics","economic model","financial model","homo economicus","rational pricing","modern portfolio theory","capital asset pricing model","black–scholes model","valuation of options","fisher separation theorem","the theory of investment value","experimental finance","vernon l. smith","journal of behavioral finance","gunduz caginalp","quantitative behavioral finance","behavioral finance","financial econometrics","actuarial science","professional qualification","quantitative analyst","computational finance","numerical analysis","mathematical model","mathematical finance","applied mathematics","modigliani–miller theorem","jurisdiction","shareholder","public limited company","management","stock exchange","asset","manufacturing","product","company","listing","corporation","italians","investor","creditor","accountant","investments","liability","business name","limited liability","corporate tax","merchandise","machine","tool","offshore financial center","handicraft","offshore company","segregated portfolio company","industry","privately held company","advertising","listing rules","pricing","parent company","economic entity","insurance","luca pacioli","finance","marketing","regulatory agency","rate of return","public finance","corporate finance","personal finance","wage labour","broker","high tech manufacturing","raw material","finished good","broadcasting","american marketing association","aviation","capital","security","digital marketing","business operations","wage","employment","treaty","trademark","copyright","patent","nasdaq","organizational studies","strategic management","operations management","service management","information technology management","people's republic of china","state-owned enterprise","commercial law","legal liability","code of hammurabi","freight transport","maurya empire","health and safety executive","trade union","public utility","initial public offering","shanghai stock exchange","intellectual property","hong kong stock exchange","new york stock exchange","occupational safety and health","trade secret","london stock exchange","working conditions","labour and employment law","collective bargaining","tokyo stock exchange","bombay stock exchange","singapore exchange","asset","finance","investing","interest","financial","business","bank","venture","portfolio","invest","arbitrage","fund","investor","speculation","diversification","capital","acquisitions","income","risk","management","assets","rate of return","investment funds","stock","investiture","profit","share","equity","commitment","invested","investors","financing","growth","development","hedge","banking","money","sector","firms","trade","revenue","securities","mutual","market","insurance","companies","shareholder","economic","profits","brokerage","holdings","debt","buy into","expenditure","outlay","hedge fund","mutual fund","time","dividend","venture capital","grooming","dressing","promotion","skin","pay","yield","cutis","pellicle","subscribe","pyramid","bull","bear","leveraging","leverage","investments","warren buffett","funds","tegument","committedness","banks","credit","statistics","managing","corporate","institutional","enterprises","firm","markets","ventures","global","partners","value","capital expenditure","businesses","savings","raise","lending","trust","boost","equities","exchange","expand","industry","loans","domestic","resources","private","corporations","acquisition","benefit","trading","diversified","projects","citigroup","expects","sachs","revenues","billion","commodity","sectors","company","dollar","overseas","deals","bankers","estate","managers","currency","costs","increase","buying","retail","commerce","dollars","purchasing","expanding","merrill","capital gain","saving","foreign direct investment","forbes","government bond","emerging markets","reinvestment","invests","capitalization","investment strategy","wealth","employment","intermediary","funding","chemise","outfit","spending","bullion","merchant","contribution","involvement","placements","vest","participation","inverter","payback","placement","lender","fiscal","fostering","input","buck","equipage","caftan","reversal","effort","costume","robe","dress","vesture","jerkin","attire","apparel","care","waistcoat","garment","custody","roi","kirtle","reverse","confinement","remand","undershirt","reversed","loan","refund","placing","modiste","frock","gown","mortgage","repayment","reimburse","capitalize","internment","tog","dressmaker","fdi","institutionalization","aum","profitability","securitization","rockport","liquidity","valuation","infrastructure","reit","greenfield","refinancing","structuring","blouse","clothe","payment","mantua","plainclothes","raiment","payout","kimono","sleeveless","garb","surety","deposit","petticoat","undergarment","vestment","wear","overall","expend","skirt","moneylender","shirt","swimsuit","wearer","pinafore","remittance","lucre","bankroll","accouter","housedress","leatherwear","innerwear","bank deposit","strapless","overdress","dressable","costumal","prestation","coatdress","nominal value","shirtdress","aguise","minidress","economics","businesswear","dirndl","sundress","underdress","lavalava","outerwear","pinny","dizen","slutwear","grubstake","simar","investissement","ofdi","sicav","sinopia","reim","shareholdings","seamark","forfaiting","overtrading","stockmarket","omers","overwear","surfwear","pridewear","divewear","unwearable","athleticwear","moneymaker","promwear","bedrape","coverall","geekwear","primp","monetize","caparison","reclothe","clubwear","beachwear","dandify","fetishwear","clothesless","nightwear","modaraba","ravewear","neckline","enclothe","vestiary","vestiment","stockingfoot","vestiture","loungewear","netherwear","designerwear","forbes 400","due diligence","earnings per share","edward o. thorp","consumption","money belt","kelly criterion","google","volatility","microsoft","earnings","mortgage lender","brokerage firm","key money","dead pledge","liquid asset","rig out","investment trust","peace dividend","fancy dress","girl clothe","dress down","woman clothe","female clothe","slide fastener","unit trust","premium bond","ao dai","cocktail dress","mother hubbard","break bank","women's clothe","blood money","pay for","fnance and economy","clothe topic","cash in hand","dress rehearsal","hussy up","french dress","protective garment","cross dress","slip on","item of clothe","ready money","ball gown","institutional investors","real estate","balanced fund","front money","form of clothe","caution money","seed money","doll up","salad cream","double denim","ready to wear","bundle up","piece of clothe","thousand island dress","pay out","dress gown","credit transfer","dollar cost averaging","woman's clothe","stark bollock naked","morning dress","operate expense","amazon.com","clothe item","man's clothe","smock frock","rent money","street clothe","princesse dress","penny pinch","banker's lien","outer wear","market timing","civilian clothe","capital gain tax","swim costume","bridge loan","medium of exchange","dollar bill","pay one's due","tank top","work clothe","lump sum","code of hammurabi","benjamin graham","david dodd","security analysis","wall street crash of 1929","price to earnings ratio","price-to-book ratio","free cash flow","earnings before interest, taxes, depreciation and amortization","working capital","capital structure","debt-to-equity ratio","mergers and acquisitions","economics","economic","saving","sector","demand","currency","inflation","finance","goods","financial","gdp","trade","production","consumption","thriftiness","barter","distribution","economic system","market economy","service","good","growth","recession","slowing","recovery","market","downturn","slowdown","unemployment","crisis","economist","markets","global","consumer","prices","outlook","weakening","exports","country","fiscal","nation","competitiveness","sentiment","protectionism","globalization","real versus nominal value","agriculture","infrastructure","capitalism","trading","service sector","technology","innovation","economical","supply","system","scheme","industrialism","efficiency","frugality","retrenchment","downsizing","curtailment","action","credit","debit","value","economize","thrifty","sociology","saver","history","save","anthropology","frugal","geography","frugalness","economically","economies","europe","sluggish","rise","conservation","weak","rising","domestic","spending","engineering","stronger","conserve","trend","boost","low-carbon","management","confidence","decline","growing","rapidly","dramatically","industry","impact","poor","emerging","expectations","robust","shrinking","slow","profession","steady","worries","improving","surplus","turmoil","falling","pushed","prospects","fall","partly","declining","slump","accelerating","interest","sectors","balance","stability","productivity","increase","weaker","rates","worried","concern","concerns","ease","driven","pushing","slowed","expanding","stabilize","reforms","rate","industrial","sees","borrowing","struggling","steadily","strong","worse","forecast","deficit","predicted","decade","woes","change","sharply","conservator","increasing","current","worsening","economizer","analysts","investment","autosave","preservation","preserve","keep","industrial relations","keeper","child labor","sumer","universal access to education","market-based economy","babylonians","retain","safeguard","defend","bergh","debt","savior","defender","guardian","preserver","mixed economy","black economy","free enterprise","laissez-faire economy","private enterprise","state socialism","non-market economy","state capitalism","economy of scale","shekel","medium of exchange","rescue","mesopotamia","protect","barley","retention","metric","savepoint","maintenance","thrift","beekeeping","donjon","guard","planned economy","withhold","keepsies","preservable","green economy","safe","savefile","freeholder","maintain","bodyguard","keepable","protector","social science","scarcity","eco","medieval","miskeep","ward","upholder","maintainable","underkeep","protective","ransom","economic sociology","chaperone","capital","defensative","defendable","economic history","defence","enshield","economic anthropology","exception","safekeeping","overkeep","bank","cautious","guardianship","economic geography","custodian","protectable","marmalade","overprotect","stronghold","prudence","expenditure","security","wary","beshield","keepalive","sentinel","company","protection","salvage","prudent","banc","goods and services","beward","foreguard","stockholder","custody","vindicate","reservatory","defense","antwerpen","fund","jailer","convoy","custodial","uphold","wite","shield","business administration","circumspect","asset","defensive","safeness","precaution","applied science","treasury","colonies","apologist","hoard","conservancy","redemption","immune","retainer","chary","preservative","spain","caretaker","cautiously","maintainer","reservation","spare","wariness","economic agent","except","portugal","expendable","economists","prosperity","tourism","finances","incomes","businesses","housing","contraction","government","employment","industries","jobs","upturn","stimulus","deflation","business","policymakers","stagnation","society","climate","eurozone","greenback","polity","macroeconomics","bankruptcies","banks","exporters","hyperinflation","dollar","entrepreneurship","workforce","deceleration","fisc","democracy","auto","population","upswing","marketplace","commerce","environment","devaluation","france","environmentalism","environmentalist","embank","quicksave","tutelage","omnium","netherlands","prophylactic","enshrine","carefulness","lifeguard","accumulation","primary sector of the economy","secondary sector of the economy","merchant","tertiary sector of the economy","life save","secularization","housekeep","nobles","degrowth","confiture","watchkeeping","real gdp","radioprotection","bankers","english language","keep off","stormproof","ancient greek","citizens","actively protect","nation-state","keep from","commodity money","fixative","watch over","grubstake","keep up","rrsp","city states","deindustrialization","stagflation","swonk","econ","disinflation","sacci","decine","stockmarket","pocketbooks","decarbonise","reflation","downspin","chier","dollarization","pinchpenny","product","withholder","bankroll","freegan","barkeeping","subsistence farming","competition","nature preserve","keep it up","body guard","anthropological","put aside","hold over","keep away","ancient greece","keep in","bond slaves","baby sit","shoot preserve","manufacturing","on defensive","mining","save game","social groups","nature reserve","transport","venture capital","physiocracy","new world","ward off","jakob fugger","world","giovanni di bicci de' medici","put by","mercantilism","postmodernism","internet","home","neoliberalism","marco polo","safe haven","mutual fund","christopher columbus","keep faith","vasco da gama","security guard","nest egg","peace dividend","plan economy","keep back","keep go","keep up with","mortgage lender","salt away","stock exchange","world bank","private sector","prison guard","save account","store away","keep in mind","keep straight","fight inflation","penny pincher","take care","keep be","fail safe","earn one's keep","unemployment rate","credit crunch","disposable income","inflationary spiral","pump priming","monetary policy","central bank","weimar republic","body politic","muddle through","durable goods","leading indicator","lagging indicator","earnest money","division of labor","financial institution","great britain","guard dog","bank rate","caution money","keynesianism","wirtschaftswunder","free trade","custom duties","public interest","secretaries of state","amschel mayer rothschild","industrial revolution","adam smith","national economy","natural price","supply and demand","thomas malthus","human overpopulation","greek language","united kingdom","north america","mass production","black market","great depression","bill clinton","world war","developing countries","economic growth","friedrich august von hayek","gross national product","john maynard keynes","revolutions of 1989","gdp per capita","social market economy","affluent society","three-sector theory","john kenneth galbraith","mass consumption economy","milton friedman"]

texttt = []

df = pd.read_csv("USFDI.csv")




print(len(df['Main_Body']))


      




def lemmatize_stemming(text):
  return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

# Tokenize and lemmatize
wordss=[]
def preprocess(text):
  for token in gensim.utils.simple_preprocess(text) :
    if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
      wordss.append(lemmatize_stemming(token))
  return wordss

for p in range (len(wordsss)):

  preprocess(wordsss[p])

final_wordss = [] 
for num in wordss: 
  if num not in final_wordss: 
    final_wordss.append(num)


def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

# Tokenize and lemmatize
result=[]
def preprocess(text):
    for token in gensim.utils.simple_preprocess(text) :
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result
  
for q in  range (0, len(df['Main_Body'])):
  df = df.dropna(axis = 0, how ='any')

  
  
print("sai")
print(len(df['Main_Body']))


for q in  range (0, len(df['Main_Body'])):
  try:
    #print(q)
    #df['Main_Body'][q].fillna('').astype(str).map(preprocess)
    #df.dropna(subset=['Main_Body'], inplace=True)

    #print(df['Main_Body'][q])
    preprocess(df['Main_Body'][q])
  except KeyError:
    continue

  
  
  
  print("Completed")
  
  results=[]

  results.append(result)
  
  result = []
  
  print(results)

  #print(results)
  #print(len(results))

  #print(final_wordss)

  dictionary = gensim.corpora.Dictionary(results)

  bow_corpus = [dictionary.doc2bow(doc) for doc in results]

  lda_model =  gensim.models.LdaMulticore(bow_corpus, 
                                   num_topics = 1, 
                                   id2word = dictionary,                                    
                                   passes = 10,
                                   workers = 2)


  for idx, topic in lda_model.print_topics(-1):
      print("Topic: {} \nWords: {}".format(idx, topic ))
      print("\n")

      output = re.sub('[^A-Za-z ]+', '', topic)




      #output = re.sub(r'\d+', '', topic)
      print (output) 

      final_list = output.split()
      print("final")
      print(final_list)
      #article['list of imp words'] = final_list



      countt = 0

      for k in final_wordss:
        for j in range (len(final_list)):
          if(final_list[j] == k):
            print(final_list[j])
            countt = countt+1


      print(countt)
      z = z + 1
      if (countt > 3):

        print(lol)
        lol=lol+1
      else:
        df.drop(df.index[z])
        
df.to_csv("Business Validated News.csv")

uploaded = drive.CreateFile({'title': "Business Validated News.csv"})

uploaded.SetContentFile("Business Validated News.csv")

uploaded.Upload()

print('Uploaded file with ID {}'.format(uploaded.get('id')))
     

"""
data = articles
      #data1 = valid_data
      df = pd.DataFrame(data)
      df.drop_duplicates(subset="title",keep="first", inplace=True)

      df.to_csv("sat_1.csv")
      print("sai")
      break







    s = substring.substringByChar("abcdefghijklmnop", startChar="([a-z]+)", endChar="([a-z]+)")
    print(s)
    
    print(topic["([a-z]+)":"([a-z]+)"])
    


results=[]

results.append(result)

print(results)

print(collections.Counter(result))


#bow = collections.Counter(result)

dictionary = gensim.corpora.Dictionary(results)

bow_corpus = [dictionary.doc2bow(doc) for doc in results]

lda_model =  gensim.models.LdaMulticore(bow_corpus, 
                                   num_topics = 8, 
                                   id2word = dictionary,                                    
                                   passes = 10,
                                   workers = 2)

for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic ))
    print("\n")

"""
b
