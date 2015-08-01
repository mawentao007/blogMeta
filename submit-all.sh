if [ $# != 1 ];  
then
        echo "usage: submit blogname"
else
        echo "**                     **"
        echo "**                     **"
        echo "****** submit blog ******"
        echo "**                     **"
        echo "**                     **"
        cd myBlog
        make publish
        cp -r .git output 
        cd output
        git add .
        git commit -m "$1"
        git push
        cp -rf .git ..
        echo "**                     **"
        echo "**                     **"
        echo "****** submit meta ******"
        echo "**                     **"
        echo "**                     **"
        cd ../../blogMeta
        git add .
        git commit -m "$1"
        git push
fi
