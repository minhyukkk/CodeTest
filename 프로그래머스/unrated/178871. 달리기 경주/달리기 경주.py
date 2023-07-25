def solution(players, callings):
    answer = []
    player_dict = {p:i for i,p in enumerate(players)} # index와 value를 value : index로 나오게 값을 바꿈
    rank_dict = {i:p for i,p in enumerate(players)}
    
    for i in callings:
        rank = player_dict[i] # 아까 바꿨으니까 이러면 등수가 나옴 
        
        player_dict[rank_dict[rank-1]], player_dict[rank_dict[rank]] = player_dict[rank_dict[rank]], player_dict[rank_dict[rank-1]]
        # player_dict[i] -> 등수가 나옴 그러면 rank_dict[]면 이름이 나오는거겠지?
        # player_dict[이름]을 해서 각자의 등수를 지금 바꾸는 작업
        
        rank_dict[rank-1], rank_dict[rank] = rank_dict[rank], rank_dict[rank-1]
        # rank_dict[] -> 숫자를 넣으면 이름이 나옴 위에서 이미 선언을 했기 떄문에 rank_dict[player_dict[rank-1]] 이런 식으로 선언을 해줄 필요 x
        # 이건 각자의 이름을 바꾸는 작업이겠지?
    
    return list(rank_dict.values())