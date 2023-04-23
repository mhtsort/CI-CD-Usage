A = [4, 2, 2; 2, 5, 2; 2, 2, 6];
e=[5,5,5,5,5]
f=[4,4,4,4]
[L, D] = v_ldl_decomposition(e,f);

disp('L:');
disp(L);
disp('D:');
disp(D);
disp('LDL*:');
disp(L * D * L');