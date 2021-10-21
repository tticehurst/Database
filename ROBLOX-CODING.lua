-- Day/Night Cycle:
while true do
    wait(0.2)
    game.Lighting.ClockTime = game.Lighting.ClockTime + 0.01
end


-- Lights turning on at night
local enabled = false

game.Lighting:GetPropertyChangedSignal("ClockTime"):Connect(function()
    local _time = game.Lighting.ClockTime

    if _time > 18 or _time < 7 then
        if not enabled then
            enabled = true
            for _,item in pairs(workspace.Map.Lights:GetDescendants()) do
                if item:IsA("Light") then
                    item.Enabled = true
                end
            end
        end

    else
        if enabled then
            enabled = false
            for _,item in pairs(workspace.Map.Lights:GetDescendants()) do
                if item:IsA("Light") then
                    item.Enabled = false
                end
            end
        end
    end
end)
