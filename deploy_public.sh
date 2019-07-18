# Build page with jekyll
jekyll build

# Sync data with S3
aws s3 sync _site s3://www.malaika.cc --exclude prev --exclude SPE --profile keim

# Create invalidation file
python3 create_invalidation_json.py _site > invbatch.json

sleep 10

# Invalidate all files
aws cloudfront create-invalidation --distribution-id E2FUHQH2ML2REJ --invalidation-batch file://invbatch.json --profile keim

# Delete invalidation file
rm invbatch.json
