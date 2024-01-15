# # from django.shortcuts import render

# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from subprocess import Popen, PIPE
# # from .models import UploadedHTML
# # from .serializers import HTMLUp/cut/cli.js test.html# # oadSerializer
# # import shlex  # Import shlex for safer shell command handling

# # class HTMLUploadView(APIView):
# #     def post(self, request, format=None):
# #         serializer = HTMLUploadSerializer(data=request.data)
# #         if serializer.is_valid():
# #             uploaded_html = serializer.save()
# #             print("fsdif")
# #             # Construct the timecut command with shlex for safer command handling
# #             command = (
# #                 f'node index.js'
# #                 # f'node C:/Users/Abhijeet/Desktop/DreelDjango/node_modules/timecut/cli.js test.html -S "#containerx" '
# #                 # f'--canvas-capture-mode --transparent-background --fps=30 --duration=5 '
# #                 # f'--pipe-mode --pix-fmt=yuv420p --output=video.mp4'
# #             )

# #             try:
# #                 # Execute the timecut command with subprocess
# #                 process = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE)
# #                 output, error = process.communicate()
# #                 print("fsdifff")
# #                 if process.returncode == 0:
# #                     return Response({'message': 'Video created successfully'}, status=status.HTTP_201_CREATED)
# #                 else:
# #                     print("fxxxxfff")
# #                     return Response({'error': error.decode()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# #             except Exception as e:
# #                 print("fsdif")
# #                 print(str(e))
# #                 return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # # Create your views here.
# # views.py
# # from django.shortcuts import render
# # from django.http import JsonResponse
# # import os
# # import subprocess
# # import json

# # def render_video_view(request):
# #     if request.method == 'POST':
# #         # Get the HTML file from the client-side POST request
# #         html_content = request.POST.get('html_content')

# #         # Save the HTML content to a temporary file
# #         html_file_path = 'templates/temp.html'
# #         with open(html_file_path, 'w') as html_file:
# #             html_file.write(html_content)

# #         # Execute the Node.js script to render the video
# #         node_script_path = 'index.js'
# #         command = f'node {node_script_path} {html_file_path}'
# #         process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #         output, error = process.communicate()

# #         # Check the return code
# #         if process.returncode == 0:
# #             response_data = {'message': 'Video created successfully'}
# #         else:
# #             response_data = {'error': error.decode()}

# #         # Clean up: Delete the temporary HTML file
# #         os.remove(html_file_path)

# #         return JsonResponse(response_data)

# #     return JsonResponse({'error': 'Invalid request method'})

# # views.py
# import os
# import subprocess
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class HTMLUploadView(APIView):
#     def post(self, request, format=None):
#         # Get the HTML content from the client-side POST request
#         # html_content = request.data.get('html_content')
#         uploaded_file = request.FILES.get('html_file')
#         # Save the HTML content to a temporary file
#         html_file_path = 'index.html'
#         with open(html_file_path, 'wb') as html_file:
#             for chunk in uploaded_file.chunks():
#                 html_file.write(chunk)
#                 print('xxx'+str(chunk))

#         try:
#             # Execute the Node.js script to render the video
#             print('efsad')
#             node_script_path = 'index.js'
#             command = f'node {node_script_path} {html_file_path}'
#             process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             output, error = process.communicate()

#             # Check the return code
#             if process.returncode == 0:
#                 print("ffs")
#                 response_data = {'message': 'Video created successfully'}
#             else:
#                 print(str(error))
#                 response_data = {'error': error.decode()}
#         finally:
#             print('done')
#             # Clean up: Delete the temporary HTML file
#             # os.remove(html_file_path)

#         return Response(response_data, status=status.HTTP_200_OK)
# views.py in yourapp
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from subprocess import Popen, PIPE
# from .serializers import HTMLUploadSerializer
# import os
# import subprocess
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# class HTMLUploadView(APIView):
#     def post(self, request, format=None):
#         serializer = HTMLUploadSerializer(data=request.data)
#         if serializer.is_valid():
#             # Save the HTML file to a model or perform any necessary processing
#             # uploaded_html = serializer.save()

#             # Check if the file exists in request.FILES
#             if 'html_file' in request.FILES:
#                 html_file = request.FILES['html_file']

#                 # Handle the uploaded file as needed
#                 # For example, save it to a temporary location
#                 with open('uploaded.html', 'wb') as destination:
#                     for chunk in html_file.chunks():
#                         destination.write(chunk)
#                         print(str(chunk))
#                 # Execute the timecut command with subprocess
#                 command = (
                    
#                     # f'node index.js'
#                     f'node C:/Users/Abhijeet/Desktop/DreelDjango/node_modules/timecut/cli.js uploaded.html -S "#containerx"  '
#                     f'--transparent-background --fps=30 --duration=5 --pipe-mode '
#                     f'--pix-fmt=yuv420p --output=videoswex.mp4'
#                 )
#                 print('cdsfsdf')
#                 process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
#                 output, error = process.communicate()

#                 if process.returncode == 0:
#                     print("dsadaf")
#                     return Response({'message': 'Video created successfully'}, status=status.HTTP_201_CREATED)
#                 else:
#                     print(str(error))
#                     return Response({'error': error.decode()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def merge_videos(request):
#     if request.method == 'POST':
#         print('dsds')
#         # Retrieve the overlay video filename from the POST request
#         overlay_filename = request.POST.get('overlayFileName', '')

#         # Specify the paths to the input and overlay videos
#         base_video_path = 'base_video.mp4'  # Replace with the actual path
#         overlay_video_path = os.path.join('/outputs', overlay_filename)  # Replace with the actual path

#         # Specify the output video path
#         output_video_path = '/merged_output.mp4'  # Replace with the desired output path

#         # FFmpeg command for merging videos with an overlay
#         ffmpeg_command = (
#             f'ffmpeg -i {base_video_path} -i {overlay_video_path} '
#             f'-filter_complex "[0:v][1:v]overlay=50:50:enable=\'between(t,5,10)\',scale=1920:1080" '
#             f'-c:v libvpx-vp9 -c:a copy {output_video_path}'
#         )

#         try:
#             # Execute the FFmpeg command with subprocess
#             process = subprocess.Popen(ffmpeg_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             output, error = process.communicate()

#             if process.returncode == 0:
#                 return JsonResponse({'message': 'Videos merged successfully'}, status=200)
#             else:
#                 return JsonResponse({'error': error.decode()}, status=500)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from subprocess import Popen, PIPE
from .serializers import HTMLUploadSerializer
import os
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class HTMLUploadView(APIView):
    def post(self, request, format=None):
        serializer = HTMLUploadSerializer(data=request.data)
        if serializer.is_valid():
            # Check if the file exists in request.FILES
            if 'html_file' in request.FILES:
                html_file = request.FILES['html_file']

                # Generate the next overlay filename
                next_filename = get_next_overlay_filename()

                # Create the 'temp' directory if it doesn't exist
                temp_directory = 'temp'
                if not os.path.exists(temp_directory):
                    os.makedirs(temp_directory)

                # Save the HTML file to a temporary location
                html_file_path = os.path.join('temp', f'{next_filename}.html')
                with open(html_file_path, 'wb') as destination:
                    for chunk in html_file.chunks():
                        destination.write(chunk)

                # Execute the timecut command with subprocess
                        print("wew")
                command = (
                    f'node C:/Users/Abhijeet/Desktop/DreelDjango/node_modules/timecut/cli.js '
                    f'{html_file_path} -S "#containerx" --transparent-background --fps=30 --duration=5 '
                    f'--pipe-mode --pix-fmt=yuva420p --output=outputs/{next_filename}.webm'
                )
                process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
                output, error = process.communicate()

                if process.returncode == 0:
                    print("dwedsdasd")
                    # Call the merge_videos function with the created video as an overlay
                    merge_videos_response = merge_videos(request, next_filename)
                    return merge_videos_response
                else:
                    print(str(error))
                    return Response({'error': error.decode()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def merge_videos(request, overlay_filename):
    if request.method == 'POST':
        # Specify the paths to the input and overlay videos
        base_video_path = 'base_video.mp4'  # Replace with the actual path
        overlay_video_path = os.path.join('outputs', f'{overlay_filename}.webm')  # Replace with the actual path

        # Specify the output video path
        output_video_path = os.path.join('outputs', f'merged_output_{overlay_filename}.mp4')  # Replace with the desired output path

        # FFmpeg command for merging videos with an overlay
        print('base_video_path')
        print('overlay_video_path')
        ffmpeg_command = (
            f"ffmpeg -i {base_video_path} -c:v libvpx-vp9 -i {overlay_video_path} -filter_complex overlay {output_video_path}"
            # f'ffmpeg -i {base_video_path} -i {overlay_video_path} '
            # f'-filter_complex "[0:v][1:v]overlay=50:50:enable=\'between(t,5,10)\',scale=1080:1920" '
            # f'-c:v libvpx-vp9 -c:a copy {output_video_path}'
        )

        try:
            # Execute the FFmpeg command with subprocess
            process = subprocess.Popen(ffmpeg_command, shell=True, stdout=PIPE, stderr=PIPE)
            output, error = process.communicate()
            
            if process.returncode == 0:
                print("Succeesssssss......")
                return JsonResponse({'message': 'Videos merged successfully'}, status=200)
            else:
                return JsonResponse({'error': error.decode()}, status=500)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_next_overlay_filename():
    # Get a list of existing files in the 'outputs' folder
    existing_files = os.listdir('outputs')

    # Filter out non-video files
    video_files = [filename for filename in existing_files if filename.endswith('.webm')]

    # Determine the next filename based on the count of existing video files
    next_filename = f'output_overlay{len(video_files) + 1:04d}'  # Format the number with leading zeros

    return next_filename
