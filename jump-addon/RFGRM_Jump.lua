-- RSL 1 experimental campaign jump-height add-on. Default: 2x.
-- Run after loading the campaign, with RSL's custom jump-height checkbox OFF.
-- Only writes Player.CodeDrivenJumpHeight; leaves VPP files and gravity alone.

RFGRMJump = RFGRMJump or { multiplier = 2, registered = false }
local state = RFGRMJump

local function log(message)
    rsl.Log("[RFGRM Jump] " .. message .. "\n")
end

local function valid(value)
    return type(value) == "number" and value > 0 and value < math.huge
end

local function close(a, b)
    return math.abs(a - b) <= 0.00001 * math.max(1, math.abs(b))
end

local function update()
    local player = Player
    if player == nil then return end
    local current = player.CodeDrivenJumpHeight
    if not valid(current) then
        if not state.warned then
            log("No positive jump-height baseline available; nothing changed. Try an ordinary jump, then run again.")
            state.warned = true
        end
        return
    end
    state.warned = false
    if state.handle ~= player.Handle then
        -- Do not treat our previous output as a fresh original on a new handle.
        if state.target and close(current, state.target) then
            log("New player handle already has the previous target; retaining the saved baseline.")
        else
            state.baseline = current
        end
        state.handle = player.Handle
    end
    if not valid(state.baseline) then return end
    local target = state.baseline * state.multiplier
    if not valid(target) then return end
    if state.target ~= target then
        log("Baseline " .. state.baseline .. "; multiplier " .. state.multiplier .. "; target " .. target)
    end
    state.target = target
    player.CodeDrivenJumpHeight = target
end

-- Invoke these functions in the RSL Lua console after running this file.
function RFGRM_SetJumpMultiplier(multiplier)
    if multiplier ~= 1 and multiplier ~= 2 and multiplier ~= 3 then
        error("Choose 1 (restore baseline), 2, or 3.")
    end
    state.multiplier = multiplier
    update()
end

if not state.registered then
    rfg.RegisterEvent("FrameUpdate", update, "RFGRM campaign jump height")
    state.registered = true
end
update()
log("Loaded. Use RFGRM_SetJumpMultiplier(2), (3), or (1) to restore the captured baseline.")
