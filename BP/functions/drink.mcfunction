#bridge-file-version: #19
scoreboard players add @p thirst 450
execute @a[scores={thirst=0..-10000}] ~ ~ ~ scoreboard players set @p thirst 0
execute @a[scores={thirst=2100..10000}] ~ ~ ~ scoreboard players set @p thirst 2099