# ##################欧拉方法解洛伦兹方程############################
# import numpy as np
# import matplotlib.pyplot as plt

# def lorenz_equations(x, y, z, σ, ρ, β):
#     dxdt = σ * (y - x)
#     dydt = x * (ρ - z) - y
#     dzdt = x * y - β * z
#     return dxdt, dydt, dzdt

# def euler_method(x0, y0, z0, σ, ρ, β, dt, num_steps):
#     t = 0
#     x_list = [x0]
#     y_list = [y0]
#     z_list = [z0]
#     t_list = [t]

#     for val in range(num_steps):
#         dxdt, dydt, dzdt = lorenz_equations(x_list[-1], y_list[-1], z_list[-1], σ, ρ, β)
#         x = x_list[-1] + dxdt * dt
#         y = y_list[-1] + dydt * dt   #核心思想x_next=x_now+x'*dt(x'可由初值跟参数推导，dt是步进)
#         z = z_list[-1] + dzdt * dt
#         x_list.append(x)
#         y_list.append(y)
#         z_list.append(z)
#         t += dt
#         t_list.append(t)

#     return t_list, x_list, y_list, z_list

# # 定义参数和初始条件
# σ = 10
# ρ = 28
# β = 8/3  #这是一个经典的参数
# x0, y0, z0 = 1, 1, 1  #全为0就没有值了
# dt = 0.01
# num_steps = 10000

# # 使用欧拉方法求解洛伦兹方程组
# t_list, x_list, y_list, z_list = euler_method(x0, y0, z0, σ, ρ, β, dt, num_steps)

# # 绘制 x 的图像
# plt.figure()
# plt.plot(t_list, x_list)
# plt.xlabel('Time')
# plt.ylabel('X')
# plt.title('X - Time')


# # 绘制 y 的图像
# plt.figure()
# plt.plot(t_list, y_list)
# plt.xlabel('Time')
# plt.ylabel('Y')
# plt.title('Y - Time')


# # 绘制 z 的图像
# plt.figure()
# plt.plot(t_list, z_list)
# plt.xlabel('Time')
# plt.ylabel('Z')
# plt.title('Z -  Time')




# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x_list, y_list, z_list)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()
















################龙格-库塔四阶###################
import numpy as np
import matplotlib.pyplot as plt
def lorenz_equations(x, y, z, σ, ρ, β):
    x_ = σ * (y - x)
    y_= x * (ρ - z) - y
    z_ = x * y - β * z
    return x_, y_, z_

def Runge_Kutta_method(x0, y0, z0, σ, ρ, β, dt, num_steps):
    t = 0
    x_list = [x0]
    y_list = [y0]
    z_list = [z0]
    t_list = [t]

    for val in range(num_steps):
        h = dt
        xk1, yk1, zk1 = lorenz_equations(x_list[-1], y_list[-1], z_list[-1], σ, ρ, β)
        xk2, yk2, zk2= lorenz_equations(x_list[-1]+xk1*h/2,y_list[-1]+yk1*h/2,z_list[-1]+zk1*h/2,σ, ρ, β)
        xk3, yk3, zk3=lorenz_equations(x_list[-1]+xk2*h/2,y_list[-1]+yk2*h/2,z_list[-1]+zk2*h/2,σ, ρ, β)
        xk4, yk4, zk4 = lorenz_equations(x_list[-1] + xk3 * h / 2, y_list[-1] + yk3 * h / 2, z_list[-1] + zk3 * h / 2, σ, ρ, β)
        x = x_list[-1] + h / 6 * (xk1 + 2 * xk2 + 2 * xk3 + xk4)
        y = y_list[-1]+  h / 6 * (yk1 + 2 * yk2 + 2 * yk3 + yk4)
        z = z_list[-1] + h / 6 * (zk1 + 2 * zk2 + 2 * zk3 + zk4)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        t += dt
        t_list.append(t)

    return t_list, x_list, y_list, z_list

# 定义参数和初始条件
σ = 10
ρ = 28
β = 8/3
x0, y0, z0 = 1, 1, 1
dt = 0.01
num_steps = 10000

# 使用龙格-库塔四阶求解洛伦兹方程组
t_list, x_list, y_list, z_list = Runge_Kutta_method(x0, y0, z0, σ, ρ, β, dt, num_steps)
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot(x_list, y_list, z_list)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')




# 绘制 x 的图像实验图在一个窗口效果不好都太小了
# ax2=fig.add_subplot(422)
# ax2.plot(t_list, x_list)
# ax2.set_xlabel('Time')
# ax2.set_ylabel('X')
# ax2.set_title('X - Time')

plt.figure()
plt.plot(t_list, x_list)
plt.xlabel('Time')
plt.ylabel('X')
plt.title('X - Time')


# 绘制 y 的图像
plt.figure()
plt.plot(t_list, y_list)
plt.xlabel('Time')
plt.ylabel('Y')
plt.title('Y - Time')


# 绘制 z 的图像
plt.figure()
plt.plot(t_list, z_list)
plt.xlabel('Time')
plt.ylabel('Z')
plt.title('Z -  Time')
plt.show()


#参考的CSDN文章
###https://blog.csdn.net/weixin_45278115/article/details/119863244
#####https://blog.csdn.net/xckkcxxck/article/details/78886701?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-78886701-blog-115421437.235%5Ev38%5Epc_relevant_anti_t3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-78886701-blog-115421437.235%5Ev38%5Epc_relevant_anti_t3&utm_relevant_index=2
####https://blog.csdn.net/weixin_42141390/article/details/110184743
######https://blog.csdn.net/wszwszwszqwer/article/details/120432428
#####https://blog.csdn.net/HelloWorldTM/article/details/112915551#:~:text=%E5%85%B7%E4%BD%93%E8%AE%A1%E7%AE%97%E5%85%AC%E5%BC%8F%E4%B8%BA%EF%BC%9A%20tn%2B1%20%3D%20tn%20%2Bh%20k1%20%3D%20f,%3D%20yn%20%2B%206h%28k1%20%2B2k2%20%2B2k3%20%2Bk4%29%20%E9%80%9A%E8%BF%87%E4%BB%A5%E4%B8%8A%E5%85%AC%E5%BC%8F%EF%BC%8C%E9%80%89%E5%8F%96%E5%90%88%E9%80%82%E7%9A%84%E6%AD%A5%E8%BF%9B%E9%95%BF%E5%BA%A6h%EF%BC%8C%E5%8F%8D%E5%A4%8D%E8%BF%AD%E4%BB%A3%EF%BC%8C%E5%B0%B1%E5%8F%AF%E6%B1%82%E8%A7%A3%E5%87%BAy%E7%9A%84%E6%95%B0%E5%80%BC%E8%A7%A3%E3%80%82