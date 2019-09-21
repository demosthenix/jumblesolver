#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int strsub(char s1[], char s2[])
{
	int i, j, c = 0;
	char copy[50];
	strcpy(copy, s1);
	for(i = 0; s2[i] != '\0'; i++)
	{
		for(j = 0; copy[j] != '\0'; j++)
		{
			if(s2[i] == copy[j])
			{
				copy[j] = '*';
				c++;
				break;
			}
		}
	}
	if(c == strlen(s2))
		return 1;
	else 
		return 0;
}

int main()
{
	char ch, letters[50], word[50];
	FILE *fp;
	printf("Enter the alphabets: ");
	scanf("%s", letters);
	printf("All possible words are as below(Extra wrong words may present):\n");
	fp = fopen("words.txt", "r");
	ch = fgetc(fp);
	while(ch != EOF)
	{
		fscanf(fp, "%[^\n]", word);
		if(strsub(letters, word) == 1 && strlen(letters) >= strlen(word))
			printf("%s\n", word); 
				
		ch = fgetc(fp);
	}
	return 0;
}
