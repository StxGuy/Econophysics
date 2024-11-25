using PyPlot

function odes(u,t)
    p,q = u
    dp = -2p*q-p^2+p
    dq = q^2+(2p-1)*q
    
    return [dp,dq]
end

function RK!(f,u,t,Δ)
    k₁ = Δ*f(u,t)
    k₂ = Δ*f(u + 0.5*k₁, t + 0.5*Δ)
    k₃ = Δ*f(u + 0.5*k₂, t + 0.5*Δ)
    k₄ = Δ*f(u + k₃, t + Δ)
    
    u .= u .+ (k₁ + 2k₂ + 2k₃ + k₄)/6
end

if true
    
    for u in ([0.15,0.5],[0.3,0.4],[0.8,0.13])
        t = 0.0
        p = []
        q = []
        r = []
        t_span = LinRange(0.0,2000.0,200)

        px = []
        py = []

        for t in t_span
            RK!(odes,u,t,0.1)
            
            x = 0.5(2u[1]+u[2])
            y = 0.5sqrt(3)*u[2]
            
            push!(px,x)
            push!(py,y)
            
            push!(p,u[1])
            push!(q,u[2])
            push!(r,1-u[1]-u[2])
        end
            
        # plot(t_span,p)
        # plot(t_span,q)
        # plot(t_span,r)
        # show()

        scatter(px,py)
    end
    
    tx = [0.0,1.0,0.5,0.0]
    ty = [0.0,0.0,1.0,0.0]
    plot(tx,ty,color="black")
    axis("off")
    text(0.5,-0.05,"p",color="blue")
    text(0,-0.05,"0",color="blue")
    text(1,-0.05,"1",color="blue")
    
    text(0.75,0.55,"q",color="red")
    text(0.515,1.0,"1",color="red")
    text(1,0,"0",color="red")
    
    text(0.15,0.55,"1-p-q",color="green")
    text(-0.025,0,"1",color="green")
    text(0.465,1,"0",color="green")
    
    savefig("RPS.svg")
    show()
end


