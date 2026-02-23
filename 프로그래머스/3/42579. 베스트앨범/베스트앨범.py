from collections import defaultdict

def solution(genres, plays):
    answer = []
    album = defaultdict(int)
    gen_songs = defaultdict(list)
    
    for i in range(len(genres)):
        album[genres[i]] += plays[i]
        gen_songs[genres[i]].append((plays[i], i))
        
    # 가장 많이 재생된 장르
    sorted_genre = sorted(album.keys(), key = lambda x: album[x], reverse=True)
    
    # 장르 내에서 가장 많이 재생된 노래
    sorted_songs = sorted(gen_songs.keys(), key = lambda x: gen_songs[x], reverse=True)
    
    # 각 장르별 상위 2개
    for genre in sorted_genre:
        songs = sorted(gen_songs[genre], key = lambda x: (-x[0], x[1]))
        
        for play, idx in songs[:2]:
            answer.append(idx)

    
    return answer

