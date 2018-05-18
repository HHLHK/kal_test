#version 330 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 newColor;


uniform vec3 newPose = vec3(0,0,0);
uniform vec3 angles= vec3(0,0,0);
uniform vec3 scale= vec3(1, 1, 1);

out vec3 color;
vec3 pos;

mat4 rotate_z(float degree){
    float rad = radians(degree);
    mat4 rotationMat = mat4(
        cos(rad),  -sin(rad),  0, 0,
        sin(rad),   cos(rad),  0, 0,
           0,       0,         1, 0,
           0,       0,          0, 1
    );
    return transpose(rotationMat);
}

mat4 rotate_y(float degree){
    float rad = radians(degree);
    mat4 rotationMat = mat4(
        cos(rad),   0,    sin(rad), 0,
        0,          1,    0, 0,
        -sin(rad),  0,    cos(rad), 0,
        0,          0,      0,      1
    );
    return transpose(rotationMat);
}

mat4 rotate_x(float degree){
    float rad = radians(degree);
    mat4 rotationMat = mat4(
        1,       0,       0,    0,
        0,  cos(rad), -sin(rad), 0,
        0,  sin(rad),  cos(rad), 0, 
        0,      0,          0, 1
    );
    return transpose(rotationMat);
}

mat4 rotate_xyz(vec3 degree){
    return rotate_x(degree[0]) * rotate_y(degree[1]) * rotate_z(degree[2]);
}

mat4 scale_xyz(vec3 k){
    mat4 m =  mat4(
        k[0], 0, 0, 0,
        0, k[1], 0, 0,
        0, 0, k[2], 0,
        0,  0,  0,  1
    );
    return transpose(m);
}

mat4 perspective(float angle, float aspect, float near, float far){
    float s = 1.0 / tan(radians(angle) / 2.0);
    float sx = s / aspect;
    float sy = s;
    float zz = (far + near) / (near - far);
    float zw = 2 * far * near / (near - far);
    mat4 m = mat4(
        sx, 0, 0, 0,
        0, sy, 0, 0,
        0, 0, zz, zw,
        0, 0, -1, 0
    );
    return m;
}

mat4 translate(vec3 moveby){
    mat4 m = mat4(
        1, 0, 0, moveby[0],
        0, 1, 0, moveby[1],
        0, 0, 1, moveby[2],
        0, 0, 0, 1
    );
    return transpose(m);
}


void main()
{
    // vec3 move = vec3(0, 0, 0);
    vec4 pos = vec4(position, 1.0);
    pos = translate(newPose) * rotate_xyz(angles) * scale_xyz(scale) * pos;
    gl_Position = pos;
    color = newColor;
}

