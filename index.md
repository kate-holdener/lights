# Holiday Lights Engineering Workshop
We are excited to have you participate in this workshop, sponsored by <a href='https://ww3.aauw.org/aauw_check/fellowships_directory/#rid6441'>American Association of University Women</a> and delivered by <a href='https://www.slu.edu/'>Saint Louis University</a>! This page contains the workshop agenda along with links to download some code examples.

### Day 1

1. Workshop instructors introductions
2. Get your supplies and begin assembying your Raspberry Pi - pocket size computer
3. Learn about your first Raspberry Pi project
  - <a href='https://www.makerspaces.com/basic-electronics/'>Basic Electronics</a>
       - Circuit
       - LED polarity
       - Resistors
       - Power and ground
  - Blinking an LED with Raspberry Pi (from the Quick-Start Guide)
4. Build the blinking LED project: 
  - <a href="screenShots/openScratch3.png">How To Open Scratch3 Environment</a>
  - <a href="screenShots/blinkingLEDCode.png">View Scratch Code</a>
  - <a href="screenShots/blinkingLED.png">View Scratch Environment</a>
  - <a href="scratch/blinkingLED.sb3" download>Download Scratch Code</a>
5. Build your 2nd project: controlling an LED with a button (use the Quick-Start Guide)
  - <a href="screenShots/buttonLED.png">View Scratch Code</a>
  - <a href="scratch/buttonLED.sb3" download>Download Scratch Code</a>
6. Discussion:
  - What skills did we use
  - What did you enjoy the most 
  - What was the most difficult part? Why was it difficult?
7. Demo of the 2nd day completed project

### Day 2

1. Demo the completed lights projects
2. Demo individual features of the lights
  - Turn on one light
  - Use different colors
  - Turn on several lights at once
  - Blink a light
3. Assemble the lights, connecting them to your Raspberry Pi
  - <a href="https://drive.google.com/file/d/1PCCHJ61IAkTXFsFqDYYFz1PIAZ4Qic5v/view?usp=sharing">Assembly Instructions</a>
4. Turn on the lights and make configuration chagnes
  - <a href="https://drive.google.com/file/d/1QCKSB7eMxPsMDTXLa3rw6IO1AajZPaeQ/view?usp=sharing">Configuration Instructions</a>
5. Download and run demo programs:
  - Rainbow Lights:
       - <a href='python/rainbowLights.py' download>Download</a>
       - <a href='https://github.com/kate-holdener/lights/blob/a7df7a0f10278c6463d92c18569bfcdb75b824ee/python/rainbowLights.py' target="_blank" rel="noopener noreferrer">View</a>
  - Random Lights:
       - <a href='python/randomLights.py' download>Download</a>
       - TODO: add comments to random lights code and add a link to view the code
6. Explain simple code examples (TODO: add links to code)
  - Turn on one light
       - <a href='https://github.com/kate-holdener/lights/blob/5a485edb7f33e692c3d9da01c40028e247acfff0/python/oneLight.py' target="_blank" rel="noopener noreferrer">View Code</a>
       - <a href='python/oneLight.py' download>Download Code</a>
  - Use different colors. <a href="https://www.rapidtables.com/web/color/RGB_Color.html" target="_blank" rel="noopener noreferrer">RGB Color Picker</a>
       - <a href='https://github.com/kate-holdener/lights/blob/5a485edb7f33e692c3d9da01c40028e247acfff0/python/differentColors.py' target="_blank" rel="noopener noreferrer">View Code</a>
       - <a href='python/differentColors.py' download>Download Code</a>
  - Turn on several lights at once
       - <a href='https://github.com/kate-holdener/lights/blob/5a485edb7f33e692c3d9da01c40028e247acfff0/python/manyLights.py' target="_blank" rel="noopener noreferrer">View Code</a>
       - <a href='python/manyLights.py' download>Download Code</a>
  - Blink a light
       - <a href='https://github.com/kate-holdener/lights/blob/5a485edb7f33e692c3d9da01c40028e247acfff0/python/blinkingLight.py' target="_blank" rel="noopener noreferrer">View Code</a>
       - <a href='python/blinkingLight.py' download>Download Code</a>
7. Try to do these:
  - Turn on all lights red
  - Turn on all lights green
  - Alternate between red and green
8. Create your own light display using the skills you learned
9. Complete the <a href="https://forms.gle/DwZqcU1aj78qzQxL6">end of workshop survey</a>
10. Disassemble your workstations and pack

## Additional Resources
Here are links to some other cool Raspberry Pi projects. Perhaps this is something you can try at home.
  - Raspberry Pi Video Door Bell
    - <a href='https://www.youtube.com/watch?v=tG_VPWNS8Sw&t=36s'>Video</a>
    - <a href='https://www.hackster.io/sneaky/fast-video-doorbell-intercom-on-raspberry-pi-63b063'>Instructions</a>
  - <a href='https://www.hackster.io/tomasz-lewicki/ai-thermometer-2bacb4#toc-7--resources-8'>AI Thermomether</a>
  - <a href='https://www.hackster.io/dominick-marino/possessed-portrait-updated-32a7a6'>Posessed Portrait</a>

## Post Workshop Resurces
1. You can create a variety of programs using the simple examples from Day 2. Use those examples as building blocks to create different light programs. You can have different files in your Home/Pi directory and alternate which one you run.
2. Remember, that to run a python program that controls your light, use this command in the terminal
<code>sudo python3 FILE_NAME.py</code>
Replace FILE_NAME.py with your own file name. When naming your files, avoid using spaces.
3. Remember to turn off your Raspberry Pi when you connect or disconnect any wires to the pins of the Raspberry Pi.
4. Remember to turn off the lights when you leave your house. Keep an eye on the lights power supply and make sure it doesn't overheat (if it starts getting too hot, turn it off).
5. If you want to get audio from your Raspberry Pi, you will need to change configurations on the Raspberry Pi:
  - In the /etc/modprobe.d/snd-blacklist.conf file, remove the <code>blacklist snd_bcm2835</code> line
  - In the /boot/config.txt file, remove the # character from #dtparam=audio=on
  - Making the above changes will allow you to play audio from your Raspberry Pi (but the lights will no longer work). You can always change the configuration back, if you want to run the lights.
