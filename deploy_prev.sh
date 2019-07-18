jekyll build
aws s3 sync _site s3://www.malaika.cc/prev --profile keim
sleep 10
aws cloudfront create-invalidation --distribution-id E2FUHQH2ML2REJ --paths /prev --profile keim
