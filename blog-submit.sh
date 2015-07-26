if [ $# != 1 ];                                                                                                                                            then
        echo "usage: submit blogname"
else
        make publish
        mv .git output 
        cd output
        git add .
        git commit -m "$1"
        git push
        mv .git ..
fi
