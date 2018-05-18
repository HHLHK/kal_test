#version 330 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 newColor;


uniform vec3 newPose = vec3(0,0,0);
uniform vec3 rotate= vec3(0,0,0);
uniform vec3 scale= vec3(1, 1, 1);

out vec3 color;
vec3 pos;

mat3 rotate_z(float degree){
    float rad = radians(degree);
    mat3 rotationMat = mat3(
        cos(rad),  -sin(rad),  0,
        sin(rad),   cos(rad),  0,
           0,       0,         1
    );
    return rotationMat;
}

mat3 rotate_y(float degree){
    float rad = radians(degree);
    mat3 rotationMat = mat3(
        cos(rad),   0,    sin(rad),
        0,          1,    0,
        -sin(rad),  0,    cos(rad)
    );
    return rotationMat;
}

mat3 rotate_x(float degree){
    float rad = radians(degree);
    mat3 rotationMat = mat3(
        1,       0,       0,
        0,  cos(rad), -sin(rad),
        0,  sin(rad),  cos(rad)
    );
    return rotationMat;
}

mat3 rotate_xyz(vec3 degree){
    return rotate_x(degree[0]) * rotate_y(degree[1]) * rotate_z(degree[2]);
}

mat3 scale_xyz(vec3 k){
    return mat3(
        k[0], 0, 0,
        0, k[1], 0,
        0, 0, k[2]
    );
}



void main()
{
    vec3 pos = position + newPose;
    
    pos =  rotate_xyz(rotate)  * scale_xyz(scale) * pos;
    gl_Position = vec4(pos, 1.0);
    color = newColor;
}

