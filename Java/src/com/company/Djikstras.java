package com.company;

import com.sun.org.apache.xpath.internal.WhitespaceStrippingElementMatcher;

import javax.xml.crypto.dsig.keyinfo.KeyValue;
import java.beans.beancontext.BeanContext;
import java.lang.reflect.Array;
import java.util.*;

/**
 * http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
 */

class DjikstrasNode
{
    public int nodeId;

    public int distToSource;

    public int sourceNodeId;

    public ArrayList<Integer> pathToSource;

    public boolean isVisited;

    public DjikstrasNode(int node, int src, int distToSource)
    {
        this.isVisited = false;
        this.nodeId = node;
        this.sourceNodeId = src;
        this.distToSource = distToSource;
        this.pathToSource = new ArrayList<>();
    }
}

public class Djikstras
{
    final static int infinity = Integer.MAX_VALUE;

    public static ArrayList<DjikstrasNode> djikstras2(int[][] verticesDist, int sourceVertex)
    {
        ArrayList<DjikstrasNode> result = new ArrayList<>();

        for (int i = 0; i < verticesDist.length; i++)
        {
            if (i == sourceVertex)
            {
                DjikstrasNode src = new DjikstrasNode(sourceVertex, sourceVertex, 0);
                src.pathToSource.add(sourceVertex);
                result.add(src);
            }
            else
            {
                DjikstrasNode node = new DjikstrasNode(i, sourceVertex, infinity);
                node.pathToSource.add(sourceVertex);
                result.add(node);
            }
        }
        int countIsVisited = 0;
        while (countIsVisited < result.size())
        {
            for (DjikstrasNode i : result)
            {
                if (i.isVisited == true)
                {
                    countIsVisited++;
                    continue;
                }
                else
                {
                    countIsVisited = 0;
                    break;
                }
            }

            if (countIsVisited == result.size())
            {
                break;
            }

            DjikstrasNode minNode = findNodeWithMinDist(result);
            minNode.isVisited = true;
            // Find adjacent nodes to the node with min dist
            ArrayList<DjikstrasNode> adjacentNodes =  findAdjacentNodes(result, minNode.nodeId, verticesDist[minNode.nodeId]);
            result = updateDistOnAdjacentNodes(adjacentNodes, result, minNode.nodeId, verticesDist[minNode.nodeId]);
        }


        return result;
    }

    public static ArrayList<DjikstrasNode> updateDistOnAdjacentNodes(ArrayList<DjikstrasNode> adjacent,
                                                                     ArrayList<DjikstrasNode> allNodes, int minNodeId,
                                                                     int[] adjacencyArray)
    {
        DjikstrasNode minNode = allNodes.get(minNodeId);

        for (DjikstrasNode node : allNodes)
        {
            for (DjikstrasNode i : adjacent)
            {
                if (i.nodeId == node.nodeId && i.isVisited == false)
                {
                    int dist = minNode.distToSource + adjacencyArray[i.nodeId];
                    if (dist < node.distToSource)
                    {
                        node.distToSource = minNode.distToSource + adjacencyArray[i.nodeId];
                    }

                }
            }

        }
        return allNodes;
    }

    public static ArrayList<DjikstrasNode> findAdjacentNodes(ArrayList<DjikstrasNode> nodes, int currentNodeId, int[] adjacencyArray)
    {
        ArrayList<DjikstrasNode> adjacentNodes = new ArrayList<>();
        for (int i = 0; i < adjacencyArray.length; i++)
        {
            if (i == currentNodeId)
                continue;
            if (adjacencyArray[i] != infinity)
            {
                adjacentNodes.add(nodes.get(i));
            }
        }
        return adjacentNodes;
    }

    public static DjikstrasNode findNodeWithMinDist(ArrayList<DjikstrasNode> nodes)
    {
        DjikstrasNode minNode = null;
        for (DjikstrasNode i : nodes)
        {
            if (i.distToSource == infinity || i.isVisited == false)
            {
                minNode = i;
                break;
            }
        }


        for (DjikstrasNode i : nodes)
        {
            if (i.distToSource <= minNode.distToSource && i.isVisited == false)
            {
                minNode = i;
            }
        }
        return minNode;
    }
    public static void djikstrasMain()
    {
        int[][] verticesDist = new int[7][7];
        verticesDist[0] = new int[] {0, infinity, 2, 5, infinity, infinity, infinity};
        verticesDist[1] = new int[] {infinity, 0, 6, infinity, infinity, infinity, infinity};
        verticesDist[2] = new int[] {2, 6, 0, 7, infinity, 1, infinity};
        verticesDist[3] = new int[] {5, infinity, 7, 0, 10, infinity, infinity};
        verticesDist[4] = new int[] {infinity, infinity, infinity, 10, 0, infinity, infinity};
        verticesDist[5] = new int[] {infinity, infinity, 1, infinity, infinity, 0, 2};
        verticesDist[6] = new int[] {infinity, infinity, infinity, infinity, infinity, 2, 0};

        djikstras2(verticesDist, 0);

    }
}
