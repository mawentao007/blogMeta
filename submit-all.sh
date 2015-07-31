if [ $# != 1 ];  
then
        echo "usage: submit blogname"
else
        echo "****** submit blog ******"
        cd myBlog
        make publish
        cp -r .git output 
        cd output
        git add .
        git commit -m "$1"
        git push
        cp -rf .git ..
        echo "****** submit meta ******"
        cd ../../blogMeta
        git add .
        git commit -m "$1"
        git push
fi
