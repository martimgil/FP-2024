def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
    }


    print("a) Table of common interests:")
    commoninterests = {(i,b): interests[i] & interests[b] for i in interests for b in interests if i != b and i<b}
    print(commoninterests)


    print("b) Maximum number of common interests:")
    maxCI = max(len(v) for v in commoninterests.values())
    print(maxCI)

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [i for i in commoninterests if len(commoninterests[i]) == maxCI]
    print(maxmatches)

    print("d) Pairs with low similarity:")
    lowJaccard = [i for i in commoninterests if len(commoninterests[i]) / len(interests[i[0]] | interests[i[1]]) < 0.25]
    print(lowJaccard)

# Start program:
main()

print("a) Tabela de interesses comuns:")