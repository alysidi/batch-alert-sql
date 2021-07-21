git submodule update --init --force --remote
cd blitz/
make build-alert-detection-proto-python LEGACY_PROTO_OUT_PATH=../proto
cd ../tests
pytest
