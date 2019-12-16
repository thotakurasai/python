import boto3
import boto

t="ECONOMY_SAUDI_TWITTERFINAL.csv"

bucketName = "rawdata-sentiment-analysis"
Key = t
outPutname = "Economy_Saudi_Twitter"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

t="ECONOMY_INDIA_TWITTERFINAL.csv"

bucketName = "rawdata-sentiment-analysis"
Key = t
outPutname = "Economy_India_Twitter"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

t="ECONOMY_UK_TWITTERFINAL.csv"

bucketName = "rawdata-sentiment-analysis"
Key = t
outPutname = "Economy_UK_Twitter"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

t="ECONOMY_USA_TWITTERFINAL.csv"

bucketName = "rawdata-sentiment-analysis"
Key = t
outPutname = "Economy_USA_Twitter"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)


t="FDIII UKK_1 - FDIII UKK_1 - in.csv"

bucketName = "rawdata-sentiment-analysis"
Key = t
outPutname = "FDI_UK_Twitter"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

t="FDIII INDIA_1 - FDIII INDIA_1 - in.csv"

bucketName = "rawdata-sentiment-analysis"
Key = t
outPutname = "FDI_India_Twitter"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

t="FDIII USA_1 - FDIII USA_1 - in.csv"

bucketName = "rawdata-sentiment-analysis"
Key = t
outPutname = "FDI_USA_Twitter"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

t="FDIII SAUDI_1 - FDIII SAUDI_1 - in.csv"

bucketName = "rawdata-sentiment-analysis"
Key = t
outPutname = "FDI_Saudi_Twitter"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

print("Done")
