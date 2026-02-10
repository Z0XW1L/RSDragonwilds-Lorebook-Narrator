local ModName = "LoreNarratorMod"
local ModActor = nil

local Defaults = {
    volume = 1.0,               -- 1.0 = full volume, 0.0 = muted
    playWhenNearLore = false,   -- true enables proximity based playing, false disables it
    searchDistance = 500.0,     -- lore scanning distance in Unreal units
    checkIntervalSeconds = 3.0, -- how often to check for nearby lore - a very low value may impact performance
    debug = false               -- prints debug messages if true. Leave it false if not needed to avoid overhead
}
local Settings = {}

local function load_settings()
    local ok, userSettings = pcall(require, "settings")
    Settings = ok and userSettings or Defaults
    setmetatable(Settings, { __index = Defaults })
    print(string.format(
        "[%s] Settings loaded. volume: %f, playWhenNearLore: %s, searchDistance: %f, checkIntervalSeconds: %f\n",
        ModName, Settings.volume, tostring(Settings.playWhenNearLore), Settings.searchDistance,
        Settings.checkIntervalSeconds))
end

local function GetActor()
    if ModActor ~= nil and ModActor:IsValid() then
        return ModActor
    end
    local ActorInstances = FindAllOf("ModActor_C")
    if not ActorInstances then
        print(string.format("[%s] No instances of 'ModActor_C' were found\n", ModName))
    else
        for Index, ActorInstance in pairs(ActorInstances) do
            if ActorInstance.PlayLore ~= nil then
                print(string.format("[%s] Found ModActor: %s\n", ModName, ActorInstance:GetFullName()))
                ModActor = ActorInstance
                return ModActor
            end
        end
        if ModActor == nil then
            print(string.format("[%s] No valid ModActor found.\n", ModName))
        end
    end
end

load_settings()

RegisterHook("/Script/Engine.PlayerController:ClientRestart", function(Context)
    print(string.format("[%s] Initializing.\n", ModName))
    local hookSuccess = pcall(function()
        print(string.format("[%s] Successfully registered interaction hook\n", ModName))
        RegisterHook(
            "Function /Game/Gameplay/World/Misc/BP_LoreItem.BP_LoreItem_C:BndEvt__BP_LoreItem_Interaction_K2Node_ComponentBoundEvent_0_OnInteraction__DelegateSignature",
            function(ContextParam, PlayerParam)
                print(string.format("[%s] Playing Lore ...\n", ModName))
                GetActor():PlayLore(PlayerParam)
            end
        )
    end)
    if not hookSuccess then
        print(string.format("[%s] Failed to register interaction hook\n", ModName))
    end
end)

RegisterCustomEvent("TransferSettings", function(Context)
    print(string.format("[%s] Transferring Settings.\n", ModName))
    if GetActor() ~= nil then
        GetActor():UpdateSettings(Settings.volume, Settings.playWhenNearLore, Settings.searchDistance,
            Settings.checkIntervalSeconds, Settings.debug, {})
    else
        print(string.format("[%s] ModActor is not (yet) valid, cannot transfer settings.\n", ModName))
    end
end)

print(string.format("[%s] Mod loaded.\n", ModName))
