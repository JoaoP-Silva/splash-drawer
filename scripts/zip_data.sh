ROOT=$(pwd)
SP_ART=$ROOT/data/splash_arts/
SKETCHES=$ROOT/data/sketches/

cd $SP_ART
zip -r images.zip ./*
cd $SKETCHES
zip -r sketches.zip ./*