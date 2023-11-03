## command-line calculator 

<p align="center">
 <img src="https://github.com/pwnedbyisa/terminal-calc/assets/138353745/c6031d80-d67c-47eb-b601-92f4ba57516c" alt="header image (that isn't rendering right if you're seeing this)"/>
</p>

___
### Overview
Welcome to my overkill calculator <3 This is a CLI tool I've been working on to expand my coding skillset (so if you see questionable formatting/ terribly written code, that's why) <br>
I'm learning as I go so any suggestions are welcome!

___
### Installation
> Python 3 should be installed on your machine for this to work optimally; I haven't fully tested for dependencies so keep that in mind
- `git clone https://github.com/pwnedbyisa/terminal-calc.git`
- cd into the `terminal-calc` directory
- `chmod -x calcadv.py` (linux)
- `python3 calcadv.py`
___
### Functions
#### Basic
```
-a, --add          <addition>
-s, --subtract     <subtraction>
-m, --multiply     <multiplication>
-d, --divide       <division>
-ex, --exponent    <exponent, [num] [exp]>
-sq, --square-root <square root>
-abs, --abs-value  <absolute value>
-l, --log          <logarithm, [num] [base]>
-f, --factorial    <return factorial (!) value>
```

#### Trig
```
-rad, --rad-from-deg <output radians from degrees>
-deg, --deg-from-rad <output degrees from radians>
-S, --sine           <sine>
-C, --cosine         <cosine>
-T, --tangent        <tangent>
-aS, --arc-sin       <inverse of sine>
-aC, --arc-cos       <inverse of cosine>
-aT, --arc-tan       <inverse of tangent>
```

#### Input Numbers
```
[e]  <e as input>
[pi] <pi as input>
```

#### Output Settings
```
-sk, --script-kiddie  <r35ult l00k5 l1k3 th15>
-em, --emoticons      <result gets one of these (´ ω ´@)>
-gm, --graphing-mode  <graph an equation - ex// -gm y=3x+2>` (heavy on the WIP w this one)
-o, --options         <options menu>
```

#### Memory
```
-mr, --memory-recall  <recall previous result(s) (up to 10)>
-mc, --memory-clear   <clear all saved results>
```

#### Help/ Resources
```
-h, --help     <help menu>
-c, --clear    <clear screen>
-git, --github <redirect to github repo>
```
___
### Currently Working On
 - getting the batch script to actually run
 - language implementation for the options menu
 - reducing dependencies
 - improving UI
 - fixing the issue where 4 extra lines print for the windows help menu (idk why)
___
### Later additions
 - actually making the graphing thing usable (there's currently no tick marks... or axes... or origin)

