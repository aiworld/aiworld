class GUID
  s4: ->
    Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1)
  create: () ->
    "#{@s4()}#{@s4()}-#{@s4()}-#{@s4()}-#{@s4()}-#{@s4()}#{@s4()}#{@s4()}"

guid = new GUID

act = ->
  $('#fais').attr('src', 'http://localhost:1235/?shoot=False&move_x=-0.585790557602&move_y=-0.0782275326677&look_x=-0.702675762832&look_y=-0.314776947275&jump=True&rand=' + guid.create());
  setTimeout act, 100

$ ->
  act()
