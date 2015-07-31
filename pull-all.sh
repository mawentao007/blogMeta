echo "****** pull Meta ******"
cd blogMeta
git pull

echo "****** pull blog ******"
cd ../myBlog
cp -rf .git output
cd output
git pull
cp -rf .git ..

