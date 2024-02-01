STAGING_SUBSTRING="_staging"



for file in ./*
do
  if [[ $file == *.model ]]; then
    new_file_name=${file//"$STAGING_SUBSTRING"/}
    echo "$file"
    echo "$new_file_name"
    mv $file $new_file_name
  fi
done


# FOO="some_staging.txt"
# FOO=${FOO//"$STAGING_SUBSTRING"/}
# echo $FOO