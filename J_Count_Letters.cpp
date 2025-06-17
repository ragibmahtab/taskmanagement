#include<bits/stdc++.h>
using namespace std;
int main()
{
   string str;
   cin>>str;
   vector<char>v(str.begin(),str.end());
   sort(v.begin(),v.end());
   vector<int>v1(26,0);
    for(char c:v)
    {
        v1[c-'a']++;
    }
    for(int i=0;i<26;i++)
    {
        if(v1[i]>0)
        cout<<char(i+'a') <<" : "<< v1[i]<<endl;
    }

    return 0;
}