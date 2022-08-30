#include <bits/stdc++.h>
using namespace std;

struct student{
int id;
float marks;
vector<int> preference;
};

bool byMarks(student first, student second){
	return first.marks > second.marks;
}
bool byId(student first, student second){
	if(first.marks==second.marks)
    return first.id < second.id;
    else return first.marks>second.marks;
}

void solve(){
    int N,C;
    cin>>C>>N;
    vector<int> array;
    array.push_back(0);
    for(int i=1;i<=C;i++){
        int temp;
        cin>>temp;
        array.push_back(temp);
    };

    vector<student> stdt;
    for(int i=0;i<N;i++){
        string str;
        cin>>str;
        vector<string> v;
        stringstream ss(str);
        while (ss.good()) {
            string subset;
            getline(ss,subset,',');
            v.push_back(subset);
        }
        struct student stdnt;
        for (size_t l = 0; l < v.size(); l++)
        {
            stdnt.id = stoi(v[0].substr(8,v[0].length()));
            stdnt.marks = stof(v[1]);
            stdnt.preference.push_back(stoi(v[2].substr(2,v[2].length())));
            stdnt.preference.push_back(stoi(v[3].substr(2,v[3].length())));
            stdnt.preference.push_back(stoi(v[4].substr(2,v[4].length())));  
        }
        stdt.push_back(stdnt);    

    }
    sort(stdt.begin(),stdt.end(),byMarks);
    sort(stdt.begin(),stdt.end(),byId);

    for(long unsigned int i=0;i<stdt.size();i++) {
        int clg;
        bool alotted=false;
        if(array[stdt[i].preference[0]]>0){
           array[stdt[i].preference[0]]--;
           alotted=true; 
           clg = stdt[i].preference[0]; 
        }
        if(!alotted && array[stdt[i].preference[1]]>0){
            array[stdt[i].preference[1]]--;
            alotted=true;
           clg = stdt[i].preference[1]; 
        }
        if(!alotted && array[stdt[i].preference[2]]>0){
            array[stdt[i].preference[2]]--;
            alotted=true;
           clg = stdt[i].preference[2]; 
        }
        if(alotted){
        string ans="";
        ans+="Student-";
        ans+=to_string(stdt[i].id);
        ans+=" C-";
        ans+=to_string(clg);
        cout<<ans;
        cout<<"\n";
        }
    };
}

signed main(){
    
    solve();
    return 0;
}