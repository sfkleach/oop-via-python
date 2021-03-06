using System;
using System.Collections.Generic;
using System.Linq;

namespace BeforeAndAfter.Before {

    public class ArticleStatus {
        public int Id { get; set; }
        public string Name { get; set; }
    }

    public class Article {
        public bool? HiddenByReviewer { get; set; }
        public ArticleStatus Status { get; set; }
        public long ReviewCode { get; set; }
        public string Name { get; set; }
    }

    public class UserFilter {
        public string Value { get; set; }
        public string Logic { get; set; }
        public string Operator { get; set; }
    }
    
    public enum TabEnum {
        WorkInProgress,
        SubmittedForReview,
        Accepted,
        Completed
    }

    public class Exercise {

        public IEnumerable<Article> FilterProposals(IEnumerable<Article> dataToFilter, UserFilter ufilter, TabEnum tab)
        {
            IEnumerable<Article> filteredData = null;

            switch (tab) {
                case TabEnum.Accepted:
                    filteredData = dataToFilter.Where(p => !p.HiddenByReviewer.HasValue || !p.HiddenByReviewer.Value);
                    break;
                case TabEnum.Completed:
                    filteredData = (
                        dataToFilter.Where(
                            p => (
                                (p.HiddenByReviewer.HasValue == true && p.HiddenByReviewer.Value == true) ||
                                (p.Status != null && p.Status.Id == 9)
                        
                            )    
                        )
                    );
                    break;
                default:
                    break;
            }

            if (ufilter != null && !string.IsNullOrEmpty(ufilter.Value))
            {
                var tmpData = filteredData ?? dataToFilter;

                if (ufilter.Logic.Equals("or") && ufilter.Operator.Equals("contains"))
                {
                    switch (tab)
                    {
                        case TabEnum.Accepted:
                        case TabEnum.Completed:
                            filteredData = tmpData.Where(t => t.Name.IndexOf(ufilter.Value, StringComparison.OrdinalIgnoreCase) >= 0 ||
                            string.Format("THING#{0}", t.ReviewCode.ToString().PadLeft(10, '0')).IndexOf(ufilter.Value, StringComparison.OrdinalIgnoreCase) >= 0);
                            break;
                        default:
                            break;
                    }
                }
            }

            return filteredData;
        }

    }
}