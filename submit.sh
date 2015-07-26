if [ $# != 1 ];                                                                                                                                            then
        echo "usage: submit blogname"
else
        mv .git output 
        cd output
        git add .
        git commit -m "$1"
        git push
        mv .git ..
fi
