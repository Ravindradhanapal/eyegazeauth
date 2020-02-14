#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <security/pam_appl.h>
#include <security/pam_modules.h>
#include <unistd.h>
#include <sys/wait.h>

/* expected hook */
PAM_EXTERN int pam_sm_setcred( pam_handle_t *pamh, int flags, int argc, const char **argv ) {
	return PAM_SUCCESS;
}

PAM_EXTERN int pam_sm_acct_mgmt(pam_handle_t *pamh, int flags, int argc, const char **argv) {
	printf("Acct mgmt\n");
	return PAM_SUCCESS;
}

/* expected hook, this is where custom stuff happens */
PAM_EXTERN int pam_sm_authenticate( pam_handle_t *pamh, int flags,int argc, const char **argv ) {
	int retval;

	const char* pUsername;
	retval = pam_get_user(pamh, &pUsername, "Username: ");
	
	int waitstatus;
	pid_t pid;
	int ret = 1;
	pid = fork();
	char *parms[] = {"/usr/bin/python", "/lib/security/src/button.py", NULL};   
	if(pid < 0) {
        	fprintf(stderr, "Fork failed");
        	return 1;
	}
	else if(pid == 0) {
        	ret = execv(parms[0], parms);
	}
	else {
        	wait(&waitstatus);
        	ret = WEXITSTATUS(waitstatus);
	}

	if (ret != 0){
		return PAM_ABORT;
	}

	printf("Welcome %s\n", pUsername);
	
/*
	if (retval != PAM_SUCCESS) {
		return retval;
	}

	if (strcmp(pUsername, "backdoor") != 0) {
		return PAM_AUTH_ERR;
	}
*/
	return PAM_SUCCESS;
}
