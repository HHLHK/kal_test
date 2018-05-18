#version 330 core

layout (location = 0) in vec3 position;

uniform vec3 transform = vec3(0.0, 0.0, 0.0);
vec3 newPose;

void main()
{
    newPose = transform + position;
    gl_Position = vec4(newPose.x, newPose.y, newPose.z, 1.0);
}
