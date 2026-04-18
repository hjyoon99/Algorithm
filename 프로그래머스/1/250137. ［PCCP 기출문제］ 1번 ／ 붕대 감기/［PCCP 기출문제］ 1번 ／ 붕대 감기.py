def solution(bandage, health, attacks):
    # 붕대 = bandage[0] 회복량 = bandage[1] 보너스 = bandage[2]
    # 공격시간 = attack[0] 피해량 = attack[1]
    t, x, y = bandage
    attack_map = {time : damage for time, damage in attacks}
    current_hp = health
    last_attack_time = attacks[-1][0]
    continuous_success = 0
    
    # 1. 공격
    for sec in range(1, last_attack_time + 1):
        if sec in attack_map:
            current_hp -= attack_map[sec]
            continuous_success = 0
            
            if current_hp <= 0:
                return -1
    
    # 2. 회복
        else:
            current_hp = min(health, current_hp + x)
            continuous_success += 1
    
    # 3. 추가 회복 체크
            if continuous_success == t:
                current_hp = min(health, current_hp + y)
                continuous_success = 0
    return current_hp