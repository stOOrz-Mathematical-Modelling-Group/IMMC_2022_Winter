initialize Q table
initialize S
choose action A from S due to a policy from Q
while not done:
    take action A, observe R, S'
    Q(S,A) <- Q(S,A)+α[R+γmaxa Q(S‘,a)−Q(S,A)]
    S <- S'
