:: 1. Run the actual packaging command
:: call "C:\Program Files\Epic Games\UE_5.x\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project="%~dp0YourProject.uproject" -clientconfig=Shipping -platform=Win64 -cook -allmaps -stage -archive -archivedirectory="%~dp0Build"

:: 2. Rename and Copy the IoStore files (*.pak, *.utoc, *.ucas)
set SOURCE_DIR=%~dp0Export\Windows\RSDragonwilds\Content\Paks
set DEST_DIR=C:\Program Files (x86)\Steam\steamapps\common\RSDragonwilds\RSDragonwilds\Content\Paks\LogicMods

set SOURCE_DIR_LUA=%~dp0..\..\mods\
set DEST_DIR_LUA=C:\Program Files (x86)\Steam\steamapps\common\RSDragonwilds\RSDragonwilds\Binaries\Win64\ue4ss\Mods

mkdir "%DEST_DIR_LUA%\LoreNarratorMod"
mkdir "%DEST_DIR_LUA%\LoreNarratorMod\Scripts"
copy "%SOURCE_DIR_LUA%\loreplayer.lua" "%DEST_DIR_LUA%\LoreNarratorMod\Scripts\main.lua"

ren "%SOURCE_DIR%\pakchunk56-Windows.pak" "LoreNarratorMod.pak"
ren "%SOURCE_DIR%\pakchunk56-Windows.utoc" "LoreNarratorMod.utoc"
ren "%SOURCE_DIR%\pakchunk56-Windows.ucas" "LoreNarratorMod.ucas"
move "%SOURCE_DIR%\LoreNarratorMod.*" "%DEST_DIR%\"
