#bridge-file-version: #27
# Bridge Version 1.34
scoreboard objectives add thirst dummy
scoreboard objectives add temperature dummy
 
execute @a[tag=!start] ~ ~ ~ scoreboard players set @p thirst 1000
execute @a[tag=!start] ~ ~ ~ scoreboard players set @p temperature 500
execute @a[tag=!start] ~ ~ ~ tag @p add start
 