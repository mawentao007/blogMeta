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
cp -rf .git ..

