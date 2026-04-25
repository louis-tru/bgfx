{
	'variables': {
		'BX_DIR%': '../bx',
		'BIMG_DIR%': '../bimg',
	},
	'target_defaults': {
		'default_configuration': 'Release',
		'configurations': {
			'Debug': {
				'defines': [ 'BX_CONFIG_DEBUG=1' ],
			},
			'Release': {
				'defines': [ 'BX_CONFIG_DEBUG=0' ],
			},
		},
		# 'cflags_cc!': [ '-std=<(std_cpp)' ],
		# 'cflags_cc+': [ '-std1=c++20' ],
		# 'xcode_settings': {
			# 'CLANG_CXX_LANGUAGE_STANDARD': 'c++20',
		# },
	},
	'targets': [
		{
			'target_name': 'libbgfx',
			'type': 'static_library',
			'direct_dependent_settings': {
				'include_dirs': [ 'include' ],
			},
			# configuration { "winstore*" }
			# 	linkoptions {
			# 		"/ignore:4264" -- LNK4264: archiving object file compiled with /ZW into a static library; note that when authoring Windows Runtime types it is not recommended to link with a static library that contains Windows Runtime metadata
			# 	}
			# configuration { "*clang*" }
			# 	buildoptions {
			# 		"-Wno-microsoft-enum-value", -- enumerator value is not representable in the underlying type 'int'
			# 		"-Wno-microsoft-const-init", -- default initialization of an object of const type '' without a user-provided default constructor is a Microsoft extension
			# 	}
			'dependencies': ['libbx', 'libbimg'],
			'defines': [
				'BGFX_CONFIG_MULTITHREADED=0', # disable multithreaded support
			],
			'include_dirs': [
				'include',
				'3rdparty',
			],
			'sources': [
				'include/bgfx/c99/bgfx.h',
				'include/bgfx/bgfx.h',
				'include/bgfx/defines.h',
				'include/bgfx/embedded_shader.h',
				'include/bgfx/platform.h',
				# 'src/amalgamated.cpp',
				'src/bgfx.cpp',
				'src/bgfx.idl.inl',
				# 'src/bgfx_compute.sh',
				'src/bgfx_p.h',
				# 'src/bgfx_shader.sh',
				'src/charset.h',
				'src/config.h',
				# 'src/cs_mipgen.sh',
				# 'src/cs_mipgen_oddx.bin.h',
				# 'src/cs_mipgen_oddx.sc',
				# 'src/cs_mipgen_oddxy.bin.h',
				# 'src/cs_mipgen_oddxy.sc',
				# 'src/cs_mipgen_oddy.bin.h',
				# 'src/cs_mipgen_oddy.sc',
				# 'src/cs_mipgen_pow2.bin.h',
				# 'src/cs_mipgen_pow2.sc',
				'src/debug_renderdoc.cpp',
				'src/debug_renderdoc.h',
				'src/dxgi.cpp',
				'src/dxgi.h',
				'src/emscripten.h',
				# 'src/fs_clear0.bin.h',
				# 'src/fs_clear0.sc',
				# 'src/fs_clear1.bin.h',
				# 'src/fs_clear1.sc',
				# 'src/fs_clear2.bin.h',
				# 'src/fs_clear2.sc',
				# 'src/fs_clear3.bin.h',
				# 'src/fs_clear3.sc',
				# 'src/fs_clear4.bin.h',
				# 'src/fs_clear4.sc',
				# 'src/fs_clear5.bin.h',
				# 'src/fs_clear5.sc',
				# 'src/fs_clear6.bin.h',
				# 'src/fs_clear6.sc',
				# 'src/fs_clear7.bin.h',
				# 'src/fs_clear7.sc',
				# 'src/fs_debugfont.bin.h',
				# 'src/fs_debugfont.sc',
				'src/glcontext_egl.cpp',
				'src/glcontext_egl.h',
				'src/glcontext_html5.cpp',
				'src/glcontext_html5.h',
				'src/glcontext_wgl.cpp',
				'src/glcontext_wgl.h',
				'src/glimports.h',
				'src/nvapi.cpp',
				'src/nvapi.h',
				'src/renderer.h',
				# 'src/renderer_agc.cpp', # PlayStation 5
				'src/renderer_gl.cpp',
				'src/renderer_gl.h',
				# 'src/renderer_gnm.cpp', # PlayStation 4
				'src/renderer_mtl.cpp',
				'src/renderer_mtl.h',
				'src/renderer_noop.cpp',
				# 'src/renderer_nvn.cpp', # Nintendo Switch
				'src/renderer_vk.cpp',
				'src/renderer_vk.h',
				# 'src/renderer_webgpu.cpp',
				# 'src/renderer_webgpu.h',
				'src/shader.cpp',
				'src/shader.h',
				'src/topology.cpp',
				'src/topology.h',
				# 'src/varying.def.sc',
				'src/version.h',
				'src/vertexlayout.cpp',
				'src/vertexlayout.h',
				# 'src/vs_clear.bin.h',
				# 'src/vs_clear.sc',
				# 'src/vs_debugfont.bin.h',
				# 'src/vs_debugfont.sc',
			],
			'conditions': [
				#define BX_PLATFORM_ANDROID    0
				#define BX_PLATFORM_BSD        0
				#define BX_PLATFORM_EMSCRIPTEN 0
				#define BX_PLATFORM_HAIKU      0
				#define BX_PLATFORM_HURD       0
				#define BX_PLATFORM_IOS        0
				#define BX_PLATFORM_LINUX      0
				#define BX_PLATFORM_NX         0
				#define BX_PLATFORM_OSX        0
				#define BX_PLATFORM_PS4        0
				#define BX_PLATFORM_PS5        0
				#define BX_PLATFORM_RPI        0
				#define BX_PLATFORM_VISIONOS   0
				#define BX_PLATFORM_WINDOWS    0
				#define BX_PLATFORM_WINRT      0
				#define BX_PLATFORM_XBOXONE    0
				['OS=="android"', {
					'ldflags': [
						# '-Wl,--fix-cortex-a8'
					],
					'defines': [
						'BGFX_CONFIG_RENDERER_OPENGLES=30', # force OpenGL ES 3.0
						'BGFX_CONFIG_RENDERER_VULKAN=1',
					],
				}],
				# configuration { "rpi" }
				# 	links {
				# 		"X11",
				# 		"brcmGLESv2",
				# 		"brcmEGL",
				# 		"bcm_host",
				# 		"vcos",
				# 		"vchiq_arm",
				# 		"pthread",
				# 	}
				['OS=="linux"', {
					'include_dirs': [
						# '3rdparty/directx-headers/include', # disable DirectX support on Linux
						# '3rdparty/directx-headers/include/directx',
						# '3rdparty/directx-headers/include/wsl/stubs',
					],
					'defines': [
						'BGFX_CONFIG_RENDERER_OPENGLES=30', # force OpenGL ES 3.0
						'BGFX_CONFIG_RENDERER_VULKAN=1',
						# 'BGFX_CONFIG_RENDERER_WEBGPU=0', # disable WebGPU support
					],
				}],
				['OS=="mac"', {
					'cflags_cc': ['-x objective-c++'],
					'defines': [
						# 'BGFX_CONFIG_RENDERER_OPENGL=33'
						'BGFX_CONFIG_RENDERER_METAL=1',
					],
				}],
				['OS=="ios"', {
					'cflags_cc': ['-x objective-c++'],
					'defines': [
						# 'BGFX_CONFIG_RENDERER_OPENGLES=30'
						'BGFX_CONFIG_RENDERER_METAL=1',
					],
				}],
				['OS=="win"', { # not durango
					'include_dirs': [
						# configuration { "vs* or mingw*", "not durango" }
						# 	includedirs {
						# 		path.join(BGFX_DIR, "3rdparty/directx-headers/include/directx"),
						# 	}
						'3rdparty/directx-headers/include/directx',
					],
					'defines': [
						# 'BGFX_CONFIG_RENDERER_OPENGL=44',
						'BGFX_CONFIG_RENDERER_DIRECT3D11=1',
						'BGFX_CONFIG_RENDERER_DIRECT3D12=1',
					],
					'sources': [
						'src/renderer_d3d.h',
						'src/renderer_d3d11.cpp',
						'src/renderer_d3d11.h',
						'src/renderer_d3d12.cpp',
						'src/renderer_d3d12.h',
					],
				}],
			],
		},
		{
			'variables': {
				'conditions': [
					['OS=="android"', {'Compat_PATH': []}],
					['OS=="linux"', {'Compat_PATH': ['<(BX_DIR)/include/compat/linux']}],
					['OS=="mac"', {'Compat_PATH': ['<(BX_DIR)/include/compat/osx']}],
					['OS=="ios"', {'Compat_PATH': ['<(BX_DIR)/include/compat/ios']}],
					['OS=="win"', {'Compat_PATH': ['<(BX_DIR)/include/compat/msvc']}],
				],
			},
			'target_name': 'libbx',
			'type': 'static_library',
			'include_dirs': [
				'<(BX_DIR)/include',
				'<(BX_DIR)/3rdparty',
				'<@(Compat_PATH)',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'<(BX_DIR)/include',
					'<@(Compat_PATH)',
				],
			},
			'defines': ['CATCH_AMALGAMATED_CUSTOM_MAIN'],
			'sources': [
				"<(BX_DIR)/src/allocator.cpp",
				"<(BX_DIR)/src/bounds.cpp",
				"<(BX_DIR)/src/bx.cpp",
				"<(BX_DIR)/src/commandline.cpp",
				"<(BX_DIR)/src/crtnone.cpp",
				"<(BX_DIR)/src/debug.cpp",
				"<(BX_DIR)/src/dtoa.cpp",
				"<(BX_DIR)/src/easing.cpp",
				"<(BX_DIR)/src/file.cpp",
				"<(BX_DIR)/src/filepath.cpp",
				"<(BX_DIR)/src/hash.cpp",
				"<(BX_DIR)/src/math.cpp",
				"<(BX_DIR)/src/mutex.cpp",
				"<(BX_DIR)/src/os.cpp",
				"<(BX_DIR)/src/process.cpp",
				"<(BX_DIR)/src/semaphore.cpp",
				"<(BX_DIR)/src/settings.cpp",
				"<(BX_DIR)/src/sort.cpp",
				"<(BX_DIR)/src/string.cpp",
				"<(BX_DIR)/src/thread.cpp",
				"<(BX_DIR)/src/timer.cpp",
				"<(BX_DIR)/src/url.cpp",
			],
		},
		{
			'target_name': 'libbimg',
			'type': 'static_library',
			'dependencies': ['libbx'],
			'defines': [
				# 'BIMG_CONFIG_PARSE_HEIF=1' # with-libheif
			],
			# configuration { "mingw* or linux* or osx*" }
			# 	buildoptions {
			# 		"-Wno-implicit-fallthrough",
			# 		"-Wno-shadow",
			# 		"-Wno-shift-negative-value",
			# 		"-Wno-undef",
			# 	}
			# 	buildoptions_cpp {
			# 		"-Wno-class-memaccess",
			# 		"-Wno-deprecated-copy",
			# 	}
			'direct_dependent_settings': {
				'include_dirs': [
					'<(BIMG_DIR)/include',
				],
			},
			'include_dirs': [
				'<(BIMG_DIR)/include',
				'<(BIMG_DIR)/3rdparty/astc-encoder/include',
				# decoders
				'<(BIMG_DIR)/3rdparty',
				'<(BIMG_DIR)/3rdparty/tinyexr/deps'
			],
			'sources': [
				# includes
				'<(BIMG_DIR)/include/bimg/bimg.h',
				'<(BIMG_DIR)/include/bimg/decode.h',
				'<(BIMG_DIR)/include/bimg/encode.h',
				# sources
				'<(BIMG_DIR)/src/bimg_p.h',
				'<(BIMG_DIR)/src/config.h',
				'<(BIMG_DIR)/src/image.cpp',
				'<(BIMG_DIR)/src/image_gnf.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_averages_and_directions.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_block_sizes.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_color_quantize.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_color_unquantize.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_compress_symbolic.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_compute_variance.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_decompress_symbolic.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_diagnostic_trace.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_diagnostic_trace.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_entry.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_find_best_partitioning.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_ideal_endpoints_and_weights.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_image.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_integer_sequence.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_internal.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_internal_entry.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_mathlib.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_mathlib.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_mathlib_softfloat.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_partition_tables.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_percentile_tables.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_pick_best_endpoint_format.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_quantization.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_symbolic_physical.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_vecmathlib.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_vecmathlib_avx2_8.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_vecmathlib_common_4.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_vecmathlib_neon_4.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_vecmathlib_none_4.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_vecmathlib_sse_4.h',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_weight_align.cpp',
				'<(BIMG_DIR)/3rdparty/astc-encoder/source/astcenc_weight_quant_xfer_tables.cpp',
				# decoders
				'<(BIMG_DIR)/src/image_decode.cpp',
			],
		},
		{
			'target_name': 'libbimg_encoder',
			'type': 'static_library',
			'dependencies': ['libbx'],
			'include_dirs': [
				'<(BIMG_DIR)/include',
				'<(BIMG_DIR)/3rdparty',
				'<(BIMG_DIR)/3rdparty/astc-encoder/include',
				'<(BIMG_DIR)/3rdparty/iqa/include',
				'<(BIMG_DIR)/3rdparty/nvtt',
				'<(BIMG_DIR)/3rdparty/tinyexr/deps/miniz',
			],
			'sources': [
				# encoders tools
				'<(BIMG_DIR)/src/image_encode.cpp',
				'<(BIMG_DIR)/src/image_cubemap_filter.cpp',
				# path.join(BIMG_DIR, "3rdparty/libsquish/**.cpp"),
				# path.join(BIMG_DIR, "3rdparty/libsquish/**.h"),
				'<(BIMG_DIR)/3rdparty/libsquish/alpha.h',
				'<(BIMG_DIR)/3rdparty/libsquish/clusterfit.h',
				'<(BIMG_DIR)/3rdparty/libsquish/colourblock.h',
				'<(BIMG_DIR)/3rdparty/libsquish/colourfit.h',
				'<(BIMG_DIR)/3rdparty/libsquish/colourset.h',
				'<(BIMG_DIR)/3rdparty/libsquish/config.h',
				'<(BIMG_DIR)/3rdparty/libsquish/maths.h',
				'<(BIMG_DIR)/3rdparty/libsquish/rangefit.h',
				'<(BIMG_DIR)/3rdparty/libsquish/simd.h',
				'<(BIMG_DIR)/3rdparty/libsquish/simd_float.h',
				'<(BIMG_DIR)/3rdparty/libsquish/singlecolourfit.h',
				'<(BIMG_DIR)/3rdparty/libsquish/squish.h',
				'<(BIMG_DIR)/3rdparty/libsquish/alpha.cpp',
				'<(BIMG_DIR)/3rdparty/libsquish/clusterfit.cpp',
				'<(BIMG_DIR)/3rdparty/libsquish/colourblock.cpp',
				'<(BIMG_DIR)/3rdparty/libsquish/colourfit.cpp',
				'<(BIMG_DIR)/3rdparty/libsquish/colourset.cpp',
				'<(BIMG_DIR)/3rdparty/libsquish/maths.cpp',
				'<(BIMG_DIR)/3rdparty/libsquish/rangefit.cpp',
				'<(BIMG_DIR)/3rdparty/libsquish/singlecolourfit.cpp',
				'<(BIMG_DIR)/3rdparty/libsquish/squish.cpp',
				# path.join(BIMG_DIR, "3rdparty/edtaa3/**.cpp"),
				# path.join(BIMG_DIR, "3rdparty/edtaa3/**.h"),
				'<(BIMG_DIR)/3rdparty/edtaa3/edtaa3func.cpp',
				'<(BIMG_DIR)/3rdparty/edtaa3/edtaa3func.h',
				# path.join(BIMG_DIR, "3rdparty/etc1/**.cpp"),
				# path.join(BIMG_DIR, "3rdparty/etc1/**.h"),
				'<(BIMG_DIR)/3rdparty/etc1/etc1.cpp',
				'<(BIMG_DIR)/3rdparty/etc1/etc1.h',
				# path.join(BIMG_DIR, "3rdparty/etc2/**.cpp"),
				# path.join(BIMG_DIR, "3rdparty/etc2/**.hpp"),
				'<(BIMG_DIR)/3rdparty/etc2/Math.hpp',
				'<(BIMG_DIR)/3rdparty/etc2/ProcessCommon.hpp',
				'<(BIMG_DIR)/3rdparty/etc2/ProcessRGB.cpp',
				'<(BIMG_DIR)/3rdparty/etc2/ProcessRGB.hpp',
				'<(BIMG_DIR)/3rdparty/etc2/Tables.cpp',
				'<(BIMG_DIR)/3rdparty/etc2/Tables.hpp',
				'<(BIMG_DIR)/3rdparty/etc2/Types.hpp',
				'<(BIMG_DIR)/3rdparty/etc2/Vector.hpp',
				# path.join(BIMG_DIR, "3rdparty/nvtt/**.cpp"),
				# path.join(BIMG_DIR, "3rdparty/nvtt/**.h"),
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_utils.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/shapes_two.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/tile.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/shapes_three.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/endpts.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/bits.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/shapes_two.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/tile.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/zoh.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/zoh_utils.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/bits.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvtt.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/utils.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/defsgnucwin32.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/debug.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/posh.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/defsgnuclinux.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/nvcore.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/stdstream.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/stream.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/defsgnucdarwin.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/foreach.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/array.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/memory.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/defsvcwin32.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/strlib.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvcore/hash.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvmath/matrix.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvmath/plane.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvmath/nvmath.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvmath/vector.h',
				'<(BIMG_DIR)/3rdparty/nvtt/nvmath/fitting.h',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_utils.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_mode7.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_mode6.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_mode4.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_mode5.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_mode1.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_mode0.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_mode2.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc7/avpcl_mode3.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/zohone.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/zoh.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/zohtwo.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/bc6h/zoh_utils.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/nvtt.cpp',
				'<(BIMG_DIR)/3rdparty/nvtt/nvmath/fitting.cpp',
				# path.join(BIMG_DIR, "3rdparty/pvrtc/**.cpp"),
				# path.join(BIMG_DIR, "3rdparty/pvrtc/**.h"),
				'<(BIMG_DIR)/3rdparty/pvrtc/AlphaBitmap.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/BitScale.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/BitUtility.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/Bitmap.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/ColorRgba.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/Interval.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/MortonTable.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/Point2.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/PvrTcDecoder.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/PvrTcEncoder.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/PvrTcPacket.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/RgbBitmap.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/RgbaBitmap.h',
				'<(BIMG_DIR)/3rdparty/pvrtc/BitScale.cpp',
				'<(BIMG_DIR)/3rdparty/pvrtc/MortonTable.cpp',
				'<(BIMG_DIR)/3rdparty/pvrtc/PvrTcDecoder.cpp',
				'<(BIMG_DIR)/3rdparty/pvrtc/PvrTcEncoder.cpp',
				'<(BIMG_DIR)/3rdparty/pvrtc/PvrTcPacket.cpp',
				# path.join(BIMG_DIR, "3rdparty/tinyexr/**.h"),
				'<(BIMG_DIR)/3rdparty/tinyexr/tinyexr.h',
				# path.join(BIMG_DIR, "3rdparty/iqa/include/**.h"),
				# path.join(BIMG_DIR, "3rdparty/iqa/source/**.c"),
				'<(BIMG_DIR)/3rdparty/iqa/include/ssim.h',
				'<(BIMG_DIR)/3rdparty/iqa/include/decimate.h',
				'<(BIMG_DIR)/3rdparty/iqa/include/iqa_os.h',
				'<(BIMG_DIR)/3rdparty/iqa/include/convolve.h',
				'<(BIMG_DIR)/3rdparty/iqa/include/math_utils.h',
				'<(BIMG_DIR)/3rdparty/iqa/include/iqa.h',
				'<(BIMG_DIR)/3rdparty/iqa/source/math_utils.c',
				'<(BIMG_DIR)/3rdparty/iqa/source/decimate.c',
				'<(BIMG_DIR)/3rdparty/iqa/source/ssim.c',
				'<(BIMG_DIR)/3rdparty/iqa/source/mse.c',
				'<(BIMG_DIR)/3rdparty/iqa/source/ms_ssim.c',
				'<(BIMG_DIR)/3rdparty/iqa/source/convolve.c',
				'<(BIMG_DIR)/3rdparty/iqa/source/psnr.c',
			],
		},
	],
}