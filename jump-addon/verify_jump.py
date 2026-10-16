"""Exercise the Lua control logic with a mocked RSL API (not a game test)."""
import ctypes
import ctypes.util
import json
from pathlib import Path


def main():
    library = ctypes.util.find_library('lua5.4')
    if not library:
        raise SystemExit('Requires a system Lua 5.4 shared library for the mock checks.')
    lua = ctypes.CDLL(library)
    lua.luaL_newstate.restype = ctypes.c_void_p
    lua.luaL_openlibs.argtypes = [ctypes.c_void_p]
    lua.luaL_loadstring.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    lua.lua_pcallk.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_longlong, ctypes.c_void_p]
    lua.lua_tolstring.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
    lua.lua_tolstring.restype = ctypes.c_char_p
    lua.lua_close.argtypes = [ctypes.c_void_p]
    script = Path(__file__).with_name('RFGRM_Jump.lua')
    fixture = 'local path = ' + json.dumps(str(script)) + '\n' + r'''
local events, registrations = {}, 0
rfg = {RegisterEvent = function(kind, callback)
    registrations = registrations + 1
    events[kind] = callback
end}
rsl = {Log = function(message) end}
local function equal(a,b) assert(math.abs(a-b)<0.00001, tostring(a)..' ~= '..tostring(b)) end
Player = {Handle=10, CodeDrivenJumpHeight=1.2, HitPoints=5500, MaxSpeed=10}
dofile(path)
equal(Player.CodeDrivenJumpHeight,2.4)
for i=1,100 do events.FrameUpdate() end
equal(Player.CodeDrivenJumpHeight,2.4)
dofile(path)
assert(registrations==1)
equal(RFGRMJump.baseline,1.2)
RFGRM_SetJumpMultiplier(3)
equal(Player.CodeDrivenJumpHeight,3.6)
RFGRM_SetJumpMultiplier(1)
equal(Player.CodeDrivenJumpHeight,1.2)
RFGRM_SetJumpMultiplier(2)
assert(Player.HitPoints==5500 and Player.MaxSpeed==10)
assert(not pcall(RFGRM_SetJumpMultiplier,4))
equal(RFGRMJump.multiplier,2)
Player={Handle=11,CodeDrivenJumpHeight=1.5}
events.FrameUpdate()
equal(Player.CodeDrivenJumpHeight,3)
Player={Handle=12,CodeDrivenJumpHeight=3}
events.FrameUpdate()
equal(Player.CodeDrivenJumpHeight,3)
equal(RFGRMJump.baseline,1.5)
Player=nil
events.FrameUpdate()
Player={Handle=13,CodeDrivenJumpHeight=0}
events.FrameUpdate()
assert(Player.CodeDrivenJumpHeight==0)
Player.CodeDrivenJumpHeight=0/0
events.FrameUpdate()
assert(Player.CodeDrivenJumpHeight~=Player.CodeDrivenJumpHeight)
Player.CodeDrivenJumpHeight=math.huge
events.FrameUpdate()
assert(Player.CodeDrivenJumpHeight==math.huge)
Player.CodeDrivenJumpHeight=1.2
events.FrameUpdate()
equal(Player.CodeDrivenJumpHeight,2.4)
RFGRM_SetJumpMultiplier(1)
equal(Player.CodeDrivenJumpHeight,1.2)
'''
    state = lua.luaL_newstate()
    if not state:
        raise RuntimeError('Could not create Lua state')
    try:
        lua.luaL_openlibs(state)
        status = lua.luaL_loadstring(state, fixture.encode())
        if status == 0:
            status = lua.lua_pcallk(state, 0, 0, 0, 0, None)
        if status:
            raise RuntimeError(lua.lua_tolstring(state, -1, None).decode())
        print('PASS: baseline scaling, 100 frames without compounding, script rerun,')
        print('2x/3x/restore, invalid selection, player replacement, nil/zero/NaN/infinity,')
        print('and unrelated player properties unchanged. Mock Lua 5.4 only; game not tested.')
    finally:
        lua.lua_close(state)


if __name__ == '__main__':
    main()
