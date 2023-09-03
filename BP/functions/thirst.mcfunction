#bridge-file-version: #46
scoreboard objectives add thirst dummy
scoreboard objectives add temperature dummy
execute @a[tag=!start] ~ ~ ~ scoreboard players set @p thirst 2100
#execute @a[tag=!start] ~ ~ ~ scoreboard players set @p temperature 500 
execute @a[tag=!start] ~ ~ ~ tag @p add start
 
scoreboard players remove @p thirst 1
 
execute @a[scores={thirst=0}] ~ ~ ~ effect @p instant_damage 1 255 true
execute @a[scores={thirst=0}] ~ ~ ~ scoreboard players set @p thirst 2100