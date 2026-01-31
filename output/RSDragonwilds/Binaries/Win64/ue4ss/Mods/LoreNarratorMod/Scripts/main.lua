ModActor = nil

local function GetActor()
    if ModActor ~= nil then
        return ModActor
    end
    local ActorInstances = FindAllOf("ModActor_C")
    if not ActorInstances then
        print("[LoreNarratorMod] No instances of 'ModActor_C' were found\n")
    else
        for Index, ActorInstance in pairs(ActorInstances) do
            if ActorInstance.PlayLore ~= nil then
                print("[LoreNarratorMod] Found ModActor: ", ActorInstance:GetFullName())
                ModActor = ActorInstance
                return ModActor
            end
        end
        if ModActor == nil then
            print("[LoreNarratorMod] No valid ModActor found.")
        end
    end
end

RegisterHook("/Script/Engine.PlayerController:ClientRestart", function (Context)
    print("[LoreNarratorMod] Initializing.")
    local hookSuccess = pcall(function()
            RegisterHook("Function /Game/Gameplay/World/Misc/BP_LoreItem.BP_LoreItem_C:BndEvt__BP_LoreItem_Interaction_K2Node_ComponentBoundEvent_0_OnInteraction__DelegateSignature",
            function(ContextParam, PlayerParam)
                print("[LoreNarratorMod] Playing Lore ...")
                GetActor():PlayLore(PlayerParam)
            end
            )
        end)
        if not hookSuccess then
            print("[LoreNarratorMod] Failed to register interaction hook")
        end
end)

print("[LoreNarratorMod] Mod loaded.\n")