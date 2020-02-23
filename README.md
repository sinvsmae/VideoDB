## Installation
system requirement:
python 3.8

## Usage
After cloning the git repo, run `.py`

# API
+ create()
+ search()
+ delete()
+ update()
+ browse()

# Schema
## Info
JSON keys:
Basics: Title, Channel, Date, Size, Format, Duration

- Preference: 难度/inspiration， 价值， 可操作性/教程，Innovation
- Progress: 1. None, 2.plan/modelling, 3. make, 4.debug/upgrade 5.Done
- Schedule: 1.<1h, 2.1-3h, 3.3-8h, 4.>1d, 5.>1w
- Craftsmanship: 1.concept, 2.prototype, 3.model, 4.product, 5.art
- Challenge: 1.very simple, 2.simple, 3.medium, 4,difficult, 5.very difficult. 加工难度， 工艺难度，（机构复杂度， 调试复杂度，电路复杂度，编程复杂度）
- Instructiveness/Informativeness: 1.overall demonstration 2.demonstrate details 3. explanation principle 4. explanation detail 6 source code/cad, detailed process; 1.appearance, 2. mechanism/detail 3.How-to
- Interactivity
- Cinematography: 1. low, casual 2.机位合理 3.带剪辑 4.带大量示例说明 5.professional


About

## Class
- Category

Keyword

Mechanical: movement, mechanism

Electronics: MCU, Sensor, Communication, IC, Analog-circuit

Make: material, machining, craft

Programming: Language, Library


```json
{ k: "value",
  k2: "va2"
}
```


# LOG


# Development
## plan
1. v1 movie mgmt
1. v1.1 setup db
1. v1.2 input records sample
1. v.1.2.1 python program to read title, channel, date
1. v.1.2.2 add other sample info
1. v1.3 setup controller, driver
1. v1.4 method
1. v2 tkinter
1. v3 html
1. v4 jQuery
