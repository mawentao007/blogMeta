echo "**                     **"
echo "**                     **"
echo "****** pull Meta ******"
echo "**                     **"
echo "**                     **"
cd blogMeta
git pull

echo "**                     **"
echo "**                     **"
echo "****** pull blog ******"
echo "**                     **"
echo "**                     **"
cd ../myBlog
cp -rf .git output
cd output
git pull
cd ..
rm -rf .git
mv  ./output/.git  ..

