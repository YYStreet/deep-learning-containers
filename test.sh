if expr "arn:aws:codebuild:us-west-2:765012582264:project/mxnet-eia-dlc-sagemaker-test-nightly" : ".*eia" >/dev/null; then
  echo "existing"
else
  echo "non"
fi