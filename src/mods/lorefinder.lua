local UEHelpers = require("UEHelpers")

ModActor = nil

local function GetActor()
    if ModActor ~= nil then
        return ModActor
    end
    local ActorInstances = FindAllOf("ModActor_C")
    if not ActorInstances then
        print("[LoreNarrator] No instances of 'ModActor_C' were found\n")
    else
        for Index, ActorInstance in pairs(ActorInstances) do
            if ActorInstance.PlayLore ~= nil then
                print("[LoreNarrator] Found ModActor: ", ActorInstance:GetFullName())
                ModActor = ActorInstance
                return ModActor
            end
        end
        if ModActor == nil then
            print("[LoreNarrator] No valid ModActor found.")
        end
    end
end

RegisterHook("/Script/Engine.PlayerController:ClientRestart", function (Context)
    print("[LoreNarrator] ClientRestart!")
    local hookSuccess = pcall(function()
            RegisterHook(
            "Function /Game/Gameplay/World/Misc/BP_LoreItem.BP_LoreItem_C:BndEvt__BP_LoreItem_Interaction_K2Node_ComponentBoundEvent_0_OnInteraction__DelegateSignature",
            function(ContextParam, PlayerParam)
                print("[LoreNarrator] Hook fired!")
                local locLoreItem = ContextParam:Get():K2_GetActorLocation()
                print("[LoreNarrator] Found Lore Item: ", ContextParam:Get():GetFullName())
                print(string.format("LOREITEM_POS: X=%.2f Y=%.2f Z=%.2f", locLoreItem.X, locLoreItem.Y, locLoreItem.Z))
                local Context = FindFirstOf("GameInstance")
                local LoreLib = StaticFindObject("/Game/Mods/FrogMod/LoreLib.Default__LoreLib_C")
                GetActor():PlayLore(PlayerParam)

                local loc = PlayerParam:Get():K2_GetActorLocation()
                if loc then
                    print(string.format("MY_POS: X=%.2f Y=%.2f Z=%.2f", loc.X, loc.Y, loc.Z))
                else
                    print(string.format("MY_POS: Location not available"))
                end
            end
            )
        end)
        if not hookSuccess then
            print("[LoreNarrator] Failed to register interaction hook")
        end
end)

local spawnedActors = {}
local spawnedActorSet = {} -- acts as a set for deduplication
local storedLocations = {}
local storedLocationSet = {} -- string-keyed set

local function AddActorOnce(actor)
    if not actor or not actor:IsValid() then
        return false
    end

    if spawnedActorSet[actor] then
        return false -- already tracked
    end

    spawnedActorSet[actor] = true
    table.insert(spawnedActors, actor)
    return true
end

local function CollectItems()
    for _, actor in ipairs(FindAllOf("BP_LoreItem_C")) do
        if AddActorOnce(actor) then
            print("[LoreNarrator] Found existing LoreItem:", actor:GetFullName())
        end
    end
end

-- Future spawns
NotifyOnNewObject("/Game/Gameplay/World/Misc/BP_LoreItem.BP_LoreItem_C", function(obj)
    if AddActorOnce(obj) then
        print("[LoreNarrator] New LoreItem spawned:", obj:GetFullName())
    end
end)

local function LocationKey(loc, precision)
    precision = precision or 2
    local x = string.format("%." .. precision .. "f", loc.X)
    local y = string.format("%." .. precision .. "f", loc.Y)
    local z = string.format("%." .. precision .. "f", loc.Z)
    return x .. "|" .. y .. "|" .. z, x, y, z
end

-- Hook key press (R)
RegisterKeyBind(0x52, function()
    CollectItems()

    print("[LoreNarrator] === BP_LoreItem Locations ===")

    for _, actor in ipairs(spawnedActors) do
        if actor and actor:IsValid() then
            local loc = actor:K2_GetActorLocation()
            if loc then
                local key, x, y, z = LocationKey(loc)

                if not storedLocationSet[key] then
                    storedLocationSet[key] = true
                    table.insert(storedLocations, { X = x, Y = y, Z = z })

                    print(string.format(
                        "[LoreNarrator] Stored location: (%s, %s, %s)",
                        x, y, z
                    ))
                end
            end
        end
    end

    -- Clear actors after harvesting
    spawnedActors = {}
    spawnedActorSet = {}

    print(string.format(
        "[LoreNarrator] Total unique locations stored: %d",
        #storedLocations
    ))
end)

-- Print press ","
RegisterKeyBind(0xBC, function()
    print("[LoreNarrator] === Stored BP_LoreItem Locations ===")
    for i, loc in ipairs(storedLocations) do
        print(string.format(
            "[LoreNarrator] [%d] (%s, %s, %s)",
            i, loc.X, loc.Y, loc.Z
        ))
    end
end)

print("[LoreNarrator] Mod loaded\n")