#!/usr/bin/env python3
"""combinatorics - Permutations and combinations."""
import sys,argparse,json,math,itertools
def main():
    p=argparse.ArgumentParser(description="Combinatorics")
    sub=p.add_subparsers(dest="cmd")
    c=sub.add_parser("choose");c.add_argument("n",type=int);c.add_argument("r",type=int)
    pe=sub.add_parser("permute");pe.add_argument("n",type=int);pe.add_argument("r",type=int,nargs="?")
    g=sub.add_parser("generate");g.add_argument("items",nargs="+");g.add_argument("--r",type=int)
    args=p.parse_args()
    if args.cmd=="choose":
        v=math.comb(args.n,args.r)
        print(json.dumps({"n":args.n,"r":args.r,"combinations":v,"with_repetition":math.comb(args.n+args.r-1,args.r)}))
    elif args.cmd=="permute":
        r=args.r or args.n;v=math.perm(args.n,r)
        print(json.dumps({"n":args.n,"r":r,"permutations":v}))
    elif args.cmd=="generate":
        r=args.r or len(args.items)
        perms=list(itertools.permutations(args.items,r))[:100]
        combs=list(itertools.combinations(args.items,r))[:100]
        print(json.dumps({"items":args.items,"r":r,"permutations":len(perms),"combinations":len(combs),"sample_perms":[list(p) for p in perms[:10]],"sample_combs":[list(c) for c in combs[:10]]}))
    else:p.print_help()
if __name__=="__main__":main()
